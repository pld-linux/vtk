# TODO:
# - handle VTK_USE_MPEG2_ENCODER (see CMakeLists.txt)
# - handle MPI and VTK_USE_PARALLEL_BGL (Parallel Boost Graph Library, BR: boost >= 1.40)
# - more system libraries? (check for VTK_THIRD_PARTY_SUBDIR in Utilities/CMakeLists.txt)
#
# Conditional build
%bcond_without	java		# Java wrappers
%bcond_without	r		# R interface
%bcond_without	sip		# Python wrappers available to SIP/PyQt
%bcond_without	ffmpeg		# FFMPEG .avi saving support
%bcond_without	odbc		# ODBC database interface
%bcond_without	chemistry	# Chemistry module (requires OpenQube)
%bcond_without	textanalysis	# TextAnalysis module (requires QtXmlPatterns)
%bcond_with	OSMesa		# build with OSMesa (https://bugzilla.redhat.com/show_bug.cgi?id=744434)
%bcond_with	system_proj	# use system PROJ.4 (needs 4.3 with exposed internals, not ready for 4.4+)
#
Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl.UTF-8):	Zestaw narzędzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
Version:	5.10.1
Release:	4
License:	BSD
Group:		Libraries
Source0:	http://www.vtk.org/files/release/5.10/%{name}-%{version}.tar.gz
# Source0-md5:	264b0052e65bd6571a84727113508789
Source1:	http://www.vtk.org/files/release/5.10/%{name}data-%{version}.tar.gz
# Source1-md5:	b6355063264cd56bcd1396c92f6ca59a
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-vtkNetCDF_cxx-soname.patch
Patch2:		%{name}-vtknetcdf-lm.patch
Patch3:		%{name}-ffmpeg.patch
Patch4:		%{name}-chemistry.patch
URL:		http://www.vtk.org/
%{?with_OSMesa:BuildRequires: Mesa-libOSMesa-devel}
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-devel
BuildRequires:	QtCore-devel >= 4.5.0
BuildRequires:	QtGui-devel >= 4.5.0
BuildRequires:	QtNetwork-devel >= 4.5.0
BuildRequires:	QtSql-devel >= 4.5.0
BuildRequires:	QtWebKit-devel >= 4.5.0
%{?with_textanalysis:BuildRequires:	QtXmlPatterns-devel >= 4.5.0}
%{?with_r:BuildRequires:	R}
BuildRequires:	boost-devel >= 1.39
BuildRequires:	cmake >= 2.6.3
BuildRequires:	doxygen
%{?with_chemistry:BuildRequires:	eigen >= 2}
BuildRequires:	expat-devel
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gl2ps-devel
BuildRequires:	gnuplot
BuildRequires:	graphviz
BuildRequires:	hdf5-devel
%if %{with java}
BuildRequires:	jdk >= 1.5
BuildRequires:  jpackage-utils
%endif
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	mysql-devel
BuildRequires:	openmotif-devel
%{?with_chemistry:BuildRequires:	openqube-devel}
BuildRequires:	postgresql-devel
%{?with_system_proj:BuildRequires:	proj-devel >= 4.3, proj-devel < 4.4}
BuildRequires:	python-devel
%{?with_sip:BuildRequires:	python-sip-devel}
BuildRequires:	qt4-build >= 4.5.0
BuildRequires:	rpmbuild(macros) >= 1.605
%{?with_sip:BuildRequires:	sip}
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRequires:	wget
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
%{?with_textanalysis:Requires:	QtXmlPatterns >= 4.5.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	lib.*Python.*\.so.*

%description
The Visualization ToolKit (VTK) is an object oriented software system
for 3D computer graphics, image processing, and visualization. VTK
includes a textbook, a C++ class library, and several interpreted
interface layers including Tcl/Tk, Java, and Python. VTK supports a
wide variety of visualization algorithms including scalar, vector,
tensor, texture, and volumetric methods. It also supports advanced
modeling techniques like implicit modeling, polygon reduction, mesh
smoothing, cutting, contouring, and Delaunay triangulation. Moreover,
dozens of imaging algorithms have been integrated into the system.
This allows mixing 2D imaging / 3D graphics algorithms and data.

%description -l pl.UTF-8
Visualization TookKit (VTK) to obiektowo zorientowany system
oprogramowania do trójwymiarowej grafiki komputerowej, przetwarzania
obrazu i wizualizacji. VTK zawiera książkę, bibliotekę klas C++ oraz
kilka interpretowanych warstw interfejsów, w tym dla Tcl/Tk, Javy i
Pythona. VTK obsługuje szeroki zakres algorytmów wizualizacji, w tym
metody skalarne, wektorowe, tensorowe, teksturowe i wolumetryczne.
Obsługuje także zaawansowane techniki modelowania, takie jak
modelowanie implicite, redukcja wielokątów, wygładzanie siatki,
przycinanie, konturowanie i triangulacja Delaunaya. Co więcej, wiele
algorytmów obrazowania zostało zintegrowanych z systemem. Pozwala to
na mieszanie algorytmów obrazowania 2D i grafiki 3D.

%package devel
Summary:	VTK header files for building C++ code
Summary(pl.UTF-8):	Pliki nagłówkowe VTK dla C++
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This provides the VTK header files required to compile C++ programs
that use VTK to do 3D visualisation.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki nagłówkowe VTK do kompilowania programów
C++ używających VTK do wizualizacji 3D.

%package qt
Summary:	Qt bindings for VTK
Summary(pl.UTF-8):	Wiązania Qt do VTK
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description qt
This package contains Qt bindings for VTK.

%description qt -l pl.UTF-8
Ten pakiet zawiera wiązania Qt do VTK.

%package qt-devel
Summary:	Header files for Qt VTK bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązania Qt do VTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	QtCore-devel
Requires:	QtGui-devel

%description qt-devel
Header files for Qt VTK bindings.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe wiązania Qt do VTK.

%package java
Summary:	Java bindings for VTK
Summary(pl.UTF-8):	Wiązania Javy do VTK
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description java
This package contains Java bindings for VTK.

%description java -l pl.UTF-8
Ten pakiet zawiera wiązania Javy do VTK.

%package java-devel
Summary:	Header files for Java VTK binding
Summary(pl.UTF-8):	Pliki nagłówkowe wiązania Javy do VTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-java = %{version}-%{release}
# <jni.h>
Requires:	jdk

%description java-devel
Header files for Java VTK binding.

%description java-devel -l pl.UTF-8
Pliki nagłówkowe wiązania Javy do VTK.

%package python
Summary:	Python bindings for VTK
Summary(pl.UTF-8):	Wiązania Pythona do VTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
This package contains Python bindings for VTK.

%description python -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona do VTK.

%package python-devel
Summary:	Header files for Python VTK binding
Summary(pl.UTF-8):	Pliki nagłówkowe wiązania Pythona do VTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-python = %{version}-%{release}
Requires:	python-devel

%description python-devel
Header files for Python VTK binding.

%description python-devel -l pl.UTF-8
Pliki nagłówkowe wiązania Pythona do VTK.

%package python-sip
Summary:	Python SIP bindings for VTK
Summary(pl.UTF-8):	Wiązania Pythona SIP do VTK
Group:		Libraries
Requires:	%{name}-python = %{version}-%{release}

%description python-sip
This package contains Python SIP bindings for VTK.

%description python-sip -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona SIP do VTK.

%package python-qt
Summary:	Python bindings for VTK Qt components
Summary(pl.UTF-8):	Wiązania Pythona do elementów Qt pakietu VTK
Group:		Libraries
Requires:	%{name}-python = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}

%description python-qt
This package contains Python bindings for VTK Qt components.

%description python-qt -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona do elementów Qt pakietu VTK.

%package tcl
Summary:	Tcl bindings for VTK
Summary(pl.UTF-8):	Wiązania języka Tcl do VTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tcl
This package contains Tcl bindings for VTK.

%description tcl -l pl.UTF-8
Ten pakiet zawiera wiązania języka Tcl do VTK.

%package tcl-devel
Summary:	Header files for Tcl VTK bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązania języka Tcl do VTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-tcl = %{version}-%{release}
Requires:	tcl-devel
Requires:	tk-devel

%description tcl-devel
Header files for Tcl VTK bindings.

%description tcl-devel -l pl.UTF-8
Pliki nagłówkowe wiązania języka Tcl do VTK.

%package examples
Summary:	C++, Tcl and Python example programs/scripts for VTK
Summary(pl.UTF-8):	Przykładowe programy/skrypty w C++, Tcl-u i Pythonie dla VTK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}

%description examples
This package contains all the examples from the VTK source. To compile
the C++ examples you will need to install the vtk-devel package as
well. The Python and Tcl examples can be run with the corresponding
packages (vtk-python, vtk-tcl).

%description examples -l pl.UTF-8
Ten pakiet zawiera wszystkie przykłady ze źródeł VTK. Do skompilowania
przykładów w C++ trzeba doinstalować pakiet vtk-devel. Przykłady w
Pythonie i Tcl-u można uruchamiać przy użyciu odpowiednich pakietów
(vtk-python, vtk-tcl).

%package test-suite
Summary:	Test programs for VTK
Summary(pl.UTF-8):	Programy testowe dla VTK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}

%description test-suite
This package contains all testing programs from the VTK source. The
source code of these programs can be found in the vtk-examples
package.

%description test-suite -l pl.UTF-8
Ten pakiet zawiera wszystkie programy testowe ze źródeł VTK. Kod
źródłowy tych programów można znaleźć w pakiecie vtk-examples.

%package data
Summary:	Data files for VTK
Summary(pl.UTF-8):	Pliki danych dla VTK
Group:		Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description data
This package contains all the data from the VTKData repository. These
data are required to run various examples from the vtk-examples
package.

%description data -l pl.UTF-8
Ten pakiet zawiera wszystkie dane z repozytorium VTKData. Dane te są
potrzebne do uruchamiania różnych przykładów z pakietu vtk-examples.

%prep
%setup -q -n VTK%{version} -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Replace relative path ../../../VTKData with %{_datadir}/vtkdata-%{version}
# otherwise it will break on symlinks.
grep -rl '\.\./\.\./\.\./\.\./VTKData' . | xargs \
  perl -pi -e's,\.\./\.\./\.\./\.\./VTKData,%{_datadir}/vtkdata-%{version},g'

# Save an unbuilt copy of the Example's sources for %doc
mkdir vtk-examples
cp -a Examples vtk-examples
# Don't ship Win32 examples
%{__rm} -r vtk-examples/Examples/GUI/Win32
find vtk-examples -type f | xargs chmod -R a-x

%build
export CFLAGS="%{rpmcflags} -D_UNICODE"
export CXXFLAGS="%{rpmcxxflags} -D_UNICODE"
%if %{with java}
export JAVA_HOME=%{java_home}
%endif

mkdir build
cd build
%cmake .. \
	-DBUILD_DOCUMENTATION:BOOL=ON \
 	-DBUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-DCMAKE_C_COMPILER:PATH="%{__cc}" \
	-DCMAKE_CXX_COMPILER:PATH="%{__cxx}" \
	-DCMAKE_LINKER_FLAGS:STRING="%{rpmldflags}" \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DOPENGL_INCLUDE_PATH:PATH=%{_includedir}/GL \
	-DPYTHON_INCLUDE_PATH:PATH=%{py_incdir} \
	-DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{py_ver}.so \
	-DPYTHON_UTIL_LIBRARY:PATH=%{_libdir}/libutil.so \
	-DTCL_INCLUDE_PATH:PATH=%{_includedir} \
	-DTCL_LIBRARY:PATH=%{_libdir}/libtcl.so \
	-DTK_INCLUDE_PATH:PATH=%{_includedir} \
	-DTK_LIBRARY:PATH=%{_libdir}/libtk.so \
	-DVTK_DATA_ROOT:PATH=%{_datadir}/vtk \
	-DVTK_INSTALL_INCLUDE_DIR:PATH=/include/vtk \
	-DVTK_INSTALL_LIB_DIR:PATH=/%{_lib}/vtk \
	-DVTK_INSTALL_QT_DIR=/%{_lib}/qt4/plugins/designer \
	%{?with_OSMesa:-DVTK_OPENGL_HAS_OSMESA:BOOL=ON} \
	-DVTK_PYTHON_SETUP_ARGS="--prefix=/usr --root=$RPM_BUILD_ROOT" \
	-DVTK_USE_SYSTEM_LIBRARIES:BOOL=ON \
	-DVTK_USE_BOOST:BOOL=ON \
	%{?with_chemistry:-DVTK_USE_CHEMISTRY:BOOL=ON} \
	%{?with_ffmpeg:-DVTK_USE_FFMPEG_ENCODER:BOOL=ON -DVTK_FFMPEG_HAS_OLD_HEADER:BOOL=OFF} \
	-DVTK_USE_GL2PS:BOOL=ON \
	%{?with_r:-DVTK_USE_GNU_R:BOOL=ON -DR_INCLUDE_DIR=/usr/include/R -DR_LIBRARY_BLAS=%{_libdir}/libblas.so -DR_LIBRARY_LAPACK=%{_libdir}/liblapack.so} \
	-DVTK_USE_GUISUPPORT:BOOL=ON \
	-DVTK_USE_MYSQL:BOOL=ON \
	%{?with_odbc:-DVTK_USE_ODBC:BOOL=ON -DODBC_LIBRARY=%{_libdir}/libodbc.so} \
	-DVTK_USE_OGGTHEORA_ENCODER:BOOL=ON \
	-DVTK_USE_PARALLEL:BOOL=ON \
	-DVTK_USE_POSTGRES:BOOL=ON \
	-DVTK_USE_QT:BOOL=ON \
	-DVTK_USE_QVTK:BOOL=ON \
	-DVTK_USE_RENDERING:BOOL=ON \
	%{!?with_system_proj:-DVTK_USE_SYSTEM_LIBPROJ4:BOOL=OFF} \
	%{?with_textanalysis:-DVTK_USE_TEXT_ANALYSIS:BOOL=ON} \
%if %{with java}
	-DVTK_WRAP_JAVA:BOOL=ON \
	-DJAVA_INCLUDE_PATH:PATH=$JAVA_HOME/include \
	-DJAVA_INCLUDE_PATH2:PATH=$JAVA_HOME/include/linux \
	-DJAVA_AWT_INCLUDE_PATH:PATH=$JAVA_HOME/include \
%else
	-DVTK_WRAP_JAVA:BOOL=OFF \
%endif
	-DVTK_WRAP_PYTHON:BOOL=ON \
	%{?with_sip:-DVTK_WRAP_PYTHON_SIP:BOOL=ON} \
	-DVTK_WRAP_TCL:BOOL=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/ld.so.conf.d,%{_examplesdir}/%{name}-%{version},%{_datadir}/vtk-data} \
	$RPM_BUILD_ROOT%{py_sitedir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# ld config
echo %{_libdir}/vtk > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/vtk-%{_arch}.conf

# fix python install path
mv $RPM_BUILD_ROOT%{py_sitescriptdir}/* $RPM_BUILD_ROOT%{py_sitedir}

cp -a VTKData%{version}/* $RPM_BUILD_ROOT%{_datadir}/vtk-data
cp -a vtk-examples/Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# Install utilities
install build/bin/lproj $RPM_BUILD_ROOT%{_bindir}

# Install examples
for f in \
HierarchicalBoxPipeline \
MultiBlock \
Arrays \
Cube \
RGrid \
SGrid \
Medical1 \
Medical2 \
Medical3 \
finance \
AmbientSpheres \
Cylinder \
DiffuseSpheres \
SpecularSpheres \
Cone \
Cone2 \
Cone3 \
Cone4 \
Cone5 \
Cone6 ; do
	install build/bin/$f $RPM_BUILD_ROOT%{_bindir}
done

# Install test binaries
for f in \
CommonCxxTests \
TestCxxFeatures \
TestInstantiator \
FilteringCxxTests \
GraphicsCxxTests \
GenericFilteringCxxTests \
ImagingCxxTests \
IOCxxTests \
RenderingCxxTests \
VTKBenchMark \
VolumeRenderingCxxTests \
WidgetsCxxTests \
SocketClient \
SocketServer ; do
	install build/bin/$f $RPM_BUILD_ROOT%{_bindir}
done

# Add exec bits to shared libs ...
#chmod 0755 %{buildroot}%{_libdir}/python*/site-packages/vtk/*.so

# Verdict places the docs in the false folder
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/vtk/doc

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%post	java -p /sbin/ldconfig
%postun	java -p /sbin/ldconfig

%post	python -p /sbin/ldconfig
%postun	python -p /sbin/ldconfig

%post	python-qt -p /sbin/ldconfig
%postun	python-qt -p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html vtkLogo.jpg vtkBanner.gif Wrapping/*/README*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ld.so.conf.d/vtk-%{_arch}.conf
%dir %{_libdir}/vtk
%attr(755,root,root) %{_libdir}/vtk/libCosmo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libCosmo.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libLSDyna.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libLSDyna.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libMapReduceMPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libMapReduceMPI.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libVPIC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libVPIC.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libmpistubs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libmpistubs.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkCharts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkCharts.so.5.10
%if %{with chemistry}
%attr(755,root,root) %{_libdir}/vtk/libvtkChemistry.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkChemistry.so.5.10
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkCommon.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkDICOMParser.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltering.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkFiltering.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFiltering.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGenericFiltering.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGeovis.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGraphics.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkHybrid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkHybrid.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkIO.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkIO.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkImaging.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkInfovis.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkNetCDF.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF_cxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkNetCDF_cxx.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkParallel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkParallel.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkRendering.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkRendering.so.5.10
%if %{with textanalysis}
%attr(755,root,root) %{_libdir}/vtk/libvtkTextAnalysis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkTextAnalysis.so.5.10
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkViews.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkViews.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRendering.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkVolumeRendering.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkWidgets.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkalglib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkalglib.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkexoIIc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkexoIIc.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkftgl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkftgl.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkmetaio.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkproj4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkproj4.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtksqlite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtksqlite.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtksys.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkverdict.so.5.10
%if %{with chemistry}
%dir %{_datadir}/vtk-5.10
%{_datadir}/vtk-5.10/vtkChemistry
%endif

%files devel
%defattr(644,root,root,755)
%doc Utilities/Upgrading/*
%attr(755,root,root) %{_bindir}/lproj
%attr(755,root,root) %{_bindir}/vtkEncodeString
%attr(755,root,root) %{_bindir}/vtkWrapHierarchy
%attr(755,root,root) %{_libdir}/vtk/libCosmo.so
%attr(755,root,root) %{_libdir}/vtk/libLSDyna.so
%attr(755,root,root) %{_libdir}/vtk/libMapReduceMPI.so
%attr(755,root,root) %{_libdir}/vtk/libVPIC.so
%attr(755,root,root) %{_libdir}/vtk/libmpistubs.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCharts.so
%if %{with chemistry}
%attr(755,root,root) %{_libdir}/vtk/libvtkChemistry.so
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFiltering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphics.so
%attr(755,root,root) %{_libdir}/vtk/libvtkHybrid.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIO.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF.so
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF_cxx.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRendering.so
%if %{with textanalysis}
%attr(755,root,root) %{_libdir}/vtk/libvtkTextAnalysis.so
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkViews.so
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRendering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgets.so
%attr(755,root,root) %{_libdir}/vtk/libvtkalglib.so
%attr(755,root,root) %{_libdir}/vtk/libvtkexoIIc.so
%attr(755,root,root) %{_libdir}/vtk/libvtkftgl.so
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so
%attr(755,root,root) %{_libdir}/vtk/libvtkproj4.so
%attr(755,root,root) %{_libdir}/vtk/libvtksqlite.so
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so
%doc %{_libdir}/vtk/doxygen
%{_libdir}/vtk/hints
%dir %{_includedir}/vtk
%{_includedir}/vtk/Cosmo
%{_includedir}/vtk/LSDyna
%{_includedir}/vtk/VPIC
%{_includedir}/vtk/alglib
%{_includedir}/vtk/internal
%{_includedir}/vtk/mrmpi
%{_includedir}/vtk/vtklibproj4
%{_includedir}/vtk/vtkmetaio
%{_includedir}/vtk/vtknetcdf
%{_includedir}/vtk/vtksqlite
%{_includedir}/vtk/vtkstd
%{_includedir}/vtk/vtksys
%{_includedir}/vtk/DICOM*.h
%{_includedir}/vtk/verdict*.h
%{_includedir}/vtk/vtk*.h
%{_includedir}/vtk/vtk*.txx
%exclude %{_includedir}/vtk/vtkEventQtSlotConnect.h
%exclude %{_includedir}/vtk/vtkJava*.h
%exclude %{_includedir}/vtk/vtkPython*.h
%exclude %{_includedir}/vtk/vtkQImageToImageSource.h
%exclude %{_includedir}/vtk/vtkQt*.h
%exclude %{_includedir}/vtk/vtkTcl*.h
%exclude %{_includedir}/vtk/vtkTk*.h
%{_libdir}/vtk/CMake
%{_libdir}/vtk/*.cmake

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libQVTK.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libQVTK.so.5.10
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libQVTKWidgetPlugin.so

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libQVTK.so
%{_includedir}/vtk/QFilterTreeProxyModel.h
%{_includedir}/vtk/QVTK*.h
%{_includedir}/vtk/vtkEventQtSlotConnect.h
%{_includedir}/vtk/vtkQImageToImageSource.h
%{_includedir}/vtk/vtkQt*.h

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vtkParseJava
%attr(755,root,root) %{_bindir}/vtkWrapJava
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkChartsJava.so.5.10
%if %{with chemistry}
%attr(755,root,root) %{_libdir}/vtk/libvtkChemistryJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkChemistryJava.so.5.10
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkCommonJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkFilteringJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkFilteringJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFilteringJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGenericFilteringJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGeovisJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphicsJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGraphicsJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkHybridJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkHybridJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkIOJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkIOJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkImagingJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkInfovisJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkParallelJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkRenderingJava.so.5.10
%if %{with textanalysis}
%attr(755,root,root) %{_libdir}/vtk/libvtkTextAnalysisJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkTextAnalysisJava.so.5.10
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkViewsJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRenderingJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkVolumeRenderingJava.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgetsJava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkWidgetsJava.so.5.10
%{_libdir}/vtk/java

%files java-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsJava.so
%if %{with chemistry}
%attr(755,root,root) %{_libdir}/vtk/libvtkChemistryJava.so
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFilteringJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFilteringJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphicsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkHybridJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingJava.so
%if %{with textanalysis}
%attr(755,root,root) %{_libdir}/vtk/libvtkTextAnalysisJava.so
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRenderingJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgetsJava.so
%{_includedir}/vtk/vtkJava*.h
%endif

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vtkWrapPython
%attr(755,root,root) %{_bindir}/vtkWrapPythonInit
%attr(755,root,root) %{_bindir}/vtkpython
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkChartsPythonD.so.5.10
%if %{with chemistry}
%attr(755,root,root) %{_libdir}/vtk/libvtkChemistryPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkChemistryPythonD.so.5.10
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkCommonPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkFilteringPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkFilteringPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFilteringPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGenericFilteringPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGeovisPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphicsPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGraphicsPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkHybridPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkHybridPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkIOPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkImagingPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkInfovisPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkParallelPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonCore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkPythonCore.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkRenderingPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingPythonTkWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkRenderingPythonTkWidgets.so.5.10
%if %{with textanalysis}
%attr(755,root,root) %{_libdir}/vtk/libvtkTextAnalysisPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkTextAnalysisPythonD.so.5.10
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkViewsPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRenderingPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkVolumeRenderingPythonD.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgetsPythonD.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkWidgetsPythonD.so.5.10
%dir %{py_sitedir}/vtk
%{py_sitedir}/vtk/*.py[co]
%dir %{py_sitedir}/vtk/gtk
%{py_sitedir}/vtk/gtk/*.py[co]
%dir %{py_sitedir}/vtk/qt
%dir %{py_sitedir}/vtk/qt4
%{py_sitedir}/vtk/qt*/*.py[co]
%dir %{py_sitedir}/vtk/test
%{py_sitedir}/vtk/test/*.py[co]
%dir %{py_sitedir}/vtk/tk
%{py_sitedir}/vtk/tk/*.py[co]
%dir %{py_sitedir}/vtk/util
%{py_sitedir}/vtk/util/*.py[co]
%dir %{py_sitedir}/vtk/wx
%{py_sitedir}/vtk/wx/*.py[co]
%attr(755,root,root) %{py_sitedir}/vtk/vtkChartsPython.so
%if %{with chemistry}
%attr(755,root,root) %{py_sitedir}/vtk/vtkChemistryPython.so
%endif
%attr(755,root,root) %{py_sitedir}/vtk/vtkCommonPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkFilteringPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkGenericFilteringPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkGeovisPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkGraphicsPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkHybridPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkIOPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkImagingPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkInfovisPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkParallelPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkRenderingPython.so
%if %{with textanalysis}
%attr(755,root,root) %{py_sitedir}/vtk/vtkTextAnalysisPython.so
%endif
%attr(755,root,root) %{py_sitedir}/vtk/vtkViewsPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkVolumeRenderingPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkWidgetsPython.so
%{py_sitedir}/VTK-%{version}-py*.egg-info

%files python-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsPythonD.so
%if %{with chemistry}
%attr(755,root,root) %{_libdir}/vtk/libvtkChemistryPythonD.so
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFilteringPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFilteringPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphicsPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkHybridPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingPythonTkWidgets.so
%if %{with textanalysis}
%attr(755,root,root) %{_libdir}/vtk/libvtkTextAnalysisPythonD.so
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRenderingPythonD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgetsPythonD.so
%{_includedir}/vtk/PyVTK*.h
%{_includedir}/vtk/vtkPython*.h

%if %{with sip}
%files python-sip
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/vtk/vtkChartsPythonSIP.so
%if %{with chemistry}
%attr(755,root,root) %{py_sitedir}/vtk/vtkChemistryPythonSIP.so
%endif
%attr(755,root,root) %{py_sitedir}/vtk/vtkCommonPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkFilteringPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkGenericFilteringPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkGeovisPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkGraphicsPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkHybridPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkIOPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkImagingPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkInfovisPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkParallelPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkRenderingPythonSIP.so
%if %{with textanalysis}
%attr(755,root,root) %{py_sitedir}/vtk/vtkTextAnalysisPythonSIP.so
%endif
%attr(755,root,root) %{py_sitedir}/vtk/vtkViewsPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkVolumeRenderingPythonSIP.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkWidgetsPythonSIP.so

%files python-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkQtPythonD.so
%attr(755,root,root) %{py_sitedir}/vtk/QVTKPython.so
%attr(755,root,root) %{py_sitedir}/vtk/vtkQtPython.so
%endif

%files tcl
%defattr(644,root,root,755)
%doc README.html vtkLogo.jpg
%attr(755,root,root) %{_bindir}/vtkWrapTcl
%attr(755,root,root) %{_bindir}/vtkWrapTclInit
%attr(755,root,root) %{_bindir}/vtk
%{_libdir}/vtk/tcl
%{_libdir}/vtk/pkgIndex.tcl
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkChartsTCL.so.5.10
%if %{with chemistry}
%attr(755,root,root) %{_libdir}/vtk/libvtkChemistryTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkChemistryTCL.so.5.10
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkCommonTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkFilteringTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkFilteringTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFilteringTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGenericFilteringTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGeovisTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphicsTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGraphicsTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkHybridTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkHybridTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkIOTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkIOTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkImagingTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkInfovisTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkParallelTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkRenderingTCL.so.5.10
%if %{with textanalysis}
%attr(755,root,root) %{_libdir}/vtk/libvtkTextAnalysisTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkTextAnalysisTCL.so.5.10
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkViewsTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRenderingTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkVolumeRenderingTCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgetsTCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkWidgetsTCL.so.5.10

%files tcl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsTCL.so
%if %{with chemistry}
%attr(755,root,root) %{_libdir}/vtk/libvtkChemistryTCL.so
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFilteringTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFilteringTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphicsTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkHybridTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingTCL.so
%if %{with textanalysis}
%attr(755,root,root) %{_libdir}/vtk/libvtkTextAnalysisTCL.so
%endif
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRenderingTCL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgetsTCL.so
%{_includedir}/vtk/vtkTcl*.h
%{_includedir}/vtk/vtkTk*.h

%files test-suite
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/CommonCxxTests
%attr(755,root,root) %{_bindir}/FilteringCxxTests
%attr(755,root,root) %{_bindir}/GenericFilteringCxxTests
%attr(755,root,root) %{_bindir}/GraphicsCxxTests
%attr(755,root,root) %{_bindir}/IOCxxTests
%attr(755,root,root) %{_bindir}/ImagingCxxTests
%attr(755,root,root) %{_bindir}/RenderingCxxTests
%attr(755,root,root) %{_bindir}/SocketClient
%attr(755,root,root) %{_bindir}/SocketServer
%attr(755,root,root) %{_bindir}/TestCxxFeatures
%attr(755,root,root) %{_bindir}/TestInstantiator
%attr(755,root,root) %{_bindir}/VTKBenchMark
%attr(755,root,root) %{_bindir}/VolumeRenderingCxxTests
%attr(755,root,root) %{_bindir}/WidgetsCxxTests
%{_libdir}/vtk/testing

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/AmbientSpheres
%attr(755,root,root) %{_bindir}/Arrays
%attr(755,root,root) %{_bindir}/Cone
%attr(755,root,root) %{_bindir}/Cone2
%attr(755,root,root) %{_bindir}/Cone3
%attr(755,root,root) %{_bindir}/Cone4
%attr(755,root,root) %{_bindir}/Cone5
%attr(755,root,root) %{_bindir}/Cone6
%attr(755,root,root) %{_bindir}/Cube
%attr(755,root,root) %{_bindir}/Cylinder
%attr(755,root,root) %{_bindir}/DiffuseSpheres
%attr(755,root,root) %{_bindir}/HierarchicalBoxPipeline
%attr(755,root,root) %{_bindir}/Medical1
%attr(755,root,root) %{_bindir}/Medical2
%attr(755,root,root) %{_bindir}/Medical3
%attr(755,root,root) %{_bindir}/MultiBlock
%attr(755,root,root) %{_bindir}/RGrid
%attr(755,root,root) %{_bindir}/SGrid
%attr(755,root,root) %{_bindir}/SpecularSpheres
%attr(755,root,root) %{_bindir}/finance
%{_examplesdir}/%{name}-%{version}

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/vtk-data
%{_datadir}/vtk-data/Baseline
%{_datadir}/vtk-data/Data
%{_datadir}/vtk-data/VTKData.readme
