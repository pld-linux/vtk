#
# TODO: package lib*(Python|Tk|Java|TCL).so somewhere?
#

# Conditional build
%bcond_without	java	# build without Java support
%bcond_with	OSMesa	# build with OSMesa (https://bugzilla.redhat.com/show_bug.cgi?id=744434)
#
Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl.UTF-8):	Zestaw narzędzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
Version:	5.10.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.vtk.org/files/release/5.10/%{name}-%{version}.tar.gz
# Source0-md5:	264b0052e65bd6571a84727113508789
Source1:	http://www.vtk.org/files/release/5.10/%{name}data-%{version}.tar.gz
# Source1-md5:	b6355063264cd56bcd1396c92f6ca59a
Patch0:		vtk-system-libs.patch
Patch1:		vtk-vtkNetCDF_cxx-soname.patch
Patch2:		vtk-vtknetcdf-lm.patch
URL:		http://www.vtk.org/
%{?with_OSMesa:BuildRequires: Mesa-libOSMesa-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	gl2ps-devel
BuildRequires:	gnuplot
BuildRequires:	graphviz
BuildRequires:	hdf5-devel
%if %{with java}
BuildRequires:	jdk
BuildRequires:  jpackage-utils
%endif
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	mysql-devel
BuildRequires:	openmotif-devel
BuildRequires:	postgresql-devel
BuildRequires:	python-devel
BuildRequires:	qt4-build
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	wget
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
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

NOTE: The Java wrapper is not included by default. You may rebuild
      the srpm using "--with java" with JDK installed.

NOTE: All patented routines which are part of the package have been
      removed in this version.

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

UWAGA: wrapper Javy nie został włączony domyślnie. Można przebudować
       srpm-a z opcją "--with java" przy zainstalowanym JDK.

UWAGA: wszystkie opatentowane procedury będące częścią tego pakietu
       zostały usunięte w tej wersji.

%package devel
Summary:	VTK header files for building C++ code
Summary(pl.UTF-8):	Pliki nagłówkowe VTK dla C++
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description devel
This provides the VTK header files required to compile C++ programs
that use VTK to do 3D visualisation.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki nagłówkowe VTK do kompilowania programów
C++ używających VTK do wizualizacji 3D.

%package tcl
Summary:	Tcl bindings for VTK
Summary(pl.UTF-8):	Wiązania Tcl do VTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tcl
This package contains Tcl bindings for VTK.

%description tcl -l pl.UTF-8
Ten pakiet zawiera wiązania Tcl do VTK.

%package python
Summary:	Python bindings for VTK
Summary(pl.UTF-8):	Wiązania Pythona do VTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
This package contains Python bindings for VTK.

%description python -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona do VTK.

%package java
Summary:	Java bindings for VTK
Summary(pl.UTF-8):	Wiązania Javy do VTK
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description java
This package contains Java bindings for VTK.

%description java -l pl.UTF-8
Ten pakiet zawiera wiązania Javy do VTK.

%package qt
Summary:	Qt bindings for VTK
Summary(pl.UTF-8):	Wiązania Qt do VTK
Requires:	vtk = %{version}-%{release}
Group:		System Environment/Libraries

%description qt
This package contains Qt bindings for VTK.

%description qt -l pl.UTF-8
Ten pakiet zawiera wiązania Qt do VTK.

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
export CFLAGS="%{optflags} -D_UNICODE"
export CXXFLAGS="%{optflags} -D_UNICODE"
%if %{with java}
export JAVA_HOME=%{java_home}
%endif

mkdir build
cd build
%{cmake} .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DVTK_INSTALL_INCLUDE_DIR:PATH=/include/vtk \
	-DVTK_INSTALL_LIB_DIR:PATH=/%{_lib}/vtk \
	-DVTK_INSTALL_QT_DIR=/%{_lib}/qt4/plugins/designer \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
 	-DBUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_DOCUMENTATION:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
%if %{with OSMesa}
	-DVTK_OPENGL_HAS_OSMESA:BOOL=ON \
%endif
%if %{with java}
	-DVTK_WRAP_JAVA:BOOL=ON \
	-DJAVA_INCLUDE_PATH:PATH=$JAVA_HOME/include \
	-DJAVA_INCLUDE_PATH2:PATH=$JAVA_HOME/include/linux \
	-DJAVA_AWT_INCLUDE_PATH:PATH=$JAVA_HOME/include \
%else
	-DVTK_WRAP_JAVA:BOOL=OFF \
%endif
	-DOPENGL_INCLUDE_PATH:PATH=%{_includedir}/GL \
	-DPYTHON_INCLUDE_PATH:PATH=%{py_incdir} \
	-DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{py_ver}.so \
	-DPYTHON_UTIL_LIBRARY:PATH=%{_libdir}/libutil.so \
	-DTCL_INCLUDE_PATH:PATH=%{_includedir} \
	-DTCL_LIBRARY:PATH=%{_libdir}/libtcl.so \
	-DTK_INCLUDE_PATH:PATH=%{_includedir} \
	-DTK_LIBRARY:PATH=%{_libdir}/libtk.so \
	-DVTK_DATA_ROOT:PATH=%{_datadir}/vtk \
	-DVTK_USE_SYSTEM_LIBRARIES=ON \
	-DVTK_USE_BOOST:BOOL=ON \
	-DVTK_USE_GL2PS:BOOL=ON \
	-DVTK_USE_GUISUPPORT:BOOL=ON \
	-DVTK_USE_MYSQL=ON \
	-DVTK_USE_OGGTHEORA_ENCODER=ON \
	-DVTK_USE_POSTGRES=ON \
	-DVTK_USE_SYSTEM_LIBPROJ4=OFF \
	-DVTK_USE_QVTK=ON \
	-DVTK_USE_QT=ON \
	-DVTK_USE_HYBRID:BOOL=ON \
	-DVTK_USE_PARALLEL:BOOL=ON \
	-DVTK_USE_PATENTED:BOOL=off \
	-DVTK_USE_RENDERING:BOOL=ON \
	-DVTK_WRAP_JAVA:BOOL=%{?with_java:ON}%{!?with_java:OFF} \
	-DVTK_PYTHON_SETUP_ARGS="--prefix=/usr --root=$RPM_BUILD_ROOT" \
	-DVTK_WRAP_PYTHON:BOOL=ON \
	-DVTK_WRAP_TCL:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_CXX_COMPILER:PATH="%{__cxx}" \
	-DCMAKE_C_COMPILER:PATH="%{__cc}" \
	-DCMAKE_LINKER_FLAGS:STRING="%{rpmldflags}" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%post	python -p /sbin/ldconfig
%postun	python -p /sbin/ldconfig

%post	java -p /sbin/ldconfig
%postun	java -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html vtkLogo.jpg vtkBanner.gif Wrapping/*/README*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ld.so.conf.d/vtk-%{_arch}.conf
%dir %{_libdir}/vtk
%attr(755,root,root) %ghost %{_libdir}/vtk/libCosmo.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libCosmo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libLSDyna.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libLSDyna.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libMapReduceMPI.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libMapReduceMPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libmpistubs.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libmpistubs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libVPIC.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libVPIC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkalglib.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkalglib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkCharts.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkCharts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkCommon.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkDICOMParser.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkexoIIc.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkexoIIc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkFiltering.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltering.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkftgl.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkftgl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGenericFiltering.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFiltering.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGeovis.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkGraphics.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkHybrid.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkHybrid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkImaging.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkInfovis.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkIO.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkIO.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkmetaio.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkNetCDF_cxx.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF_cxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkNetCDF.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkParallel.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkParallel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkproj4.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkproj4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkRendering.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkRendering.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtksqlite.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtksqlite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtksys.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkverdict.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkViews.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkViews.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkVolumeRendering.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRendering.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtkWidgets.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgets.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc %{_libdir}/vtk/doxygen
%doc Utilities/Upgrading/*
%attr(755,root,root) %{_bindir}/vtkWrapHierarchy
%attr(755,root,root) %{_bindir}/lproj
%attr(755,root,root) %{_bindir}/vtkEncodeString
%{_includedir}/vtk
%{_libdir}/vtk/CMake
%{_libdir}/vtk/*.cmake
%{_libdir}/vtk/hints
%attr(755,root,root) %{_libdir}/vtk/libCosmo.so
%attr(755,root,root) %{_libdir}/vtk/libLSDyna.so
%attr(755,root,root) %{_libdir}/vtk/libMapReduceMPI.so
%attr(755,root,root) %{_libdir}/vtk/libmpistubs.so
%attr(755,root,root) %{_libdir}/vtk/libVPIC.so
%attr(755,root,root) %{_libdir}/vtk/libvtkalglib.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCharts.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so
%attr(755,root,root) %{_libdir}/vtk/libvtkexoIIc.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkftgl.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGenericFiltering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphics.so
%attr(755,root,root) %{_libdir}/vtk/libvtkHybrid.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIO.so
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF_cxx.so
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkproj4.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRendering.so
%attr(755,root,root) %{_libdir}/vtk/libvtksqlite.so
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViews.so
%attr(755,root,root) %{_libdir}/vtk/libvtkVolumeRendering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWidgets.so

%files tcl
%defattr(644,root,root,755)
%doc README.html vtkLogo.jpg
%attr(755,root,root) %{_bindir}/vtkWrapTcl
%attr(755,root,root) %{_bindir}/vtkWrapTclInit
%attr(755,root,root) %{_bindir}/vtk
%{_libdir}/vtk/tcl
%{_libdir}/vtk/pkgIndex.tcl
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtk*TCL.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtk*TCL.so.*.*.*

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vtkWrapPython
%attr(755,root,root) %{_bindir}/vtkWrapPythonInit
%attr(755,root,root) %{_bindir}/vtkpython
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtk*Python*.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtk*Python*.so.*.*.*

%dir %{py_sitedir}/vtk
%{py_sitedir}/vtk/*.py*
%dir %{py_sitedir}/vtk/gtk
%{py_sitedir}/vtk/gtk/*.py*
%dir %{py_sitedir}/vtk/qt
%dir %{py_sitedir}/vtk/qt4
%{py_sitedir}/vtk/qt*/*.py*
%dir %{py_sitedir}/vtk/test
%{py_sitedir}/vtk/test/*.py*
%dir %{py_sitedir}/vtk/tk
%{py_sitedir}/vtk/tk/*.py*
%dir %{py_sitedir}/vtk/util
%{py_sitedir}/vtk/util/*.py*
%dir %{py_sitedir}/vtk/wx
%{py_sitedir}/vtk/wx/*.py*
%attr(755,root,root) %{py_sitedir}/vtk/vtk*.so
%{py_sitedir}/VTK-%{version}-*.egg-info

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vtkParseJava
%attr(755,root,root) %{_bindir}/vtkWrapJava
%attr(755,root,root) %ghost %{_libdir}/vtk/libvtk*Java.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libvtk*Java.so.*.*.*
%{_libdir}/vtk/java
%endif

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/vtk/libQVTK.so.5.10
%attr(755,root,root) %{_libdir}/vtk/libQVTK.so.*.*.*
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libQVTKWidgetPlugin.so

%files test-suite
%defattr(644,root,root,755)
%{_libdir}/vtk/testing
%attr(755,root,root) %{_bindir}/CommonCxxTests
%attr(755,root,root) %{_bindir}/TestCxxFeatures
%attr(755,root,root) %{_bindir}/TestInstantiator
%attr(755,root,root) %{_bindir}/FilteringCxxTests
%attr(755,root,root) %{_bindir}/GraphicsCxxTests
%attr(755,root,root) %{_bindir}/GenericFilteringCxxTests
%attr(755,root,root) %{_bindir}/ImagingCxxTests
%attr(755,root,root) %{_bindir}/IOCxxTests
%attr(755,root,root) %{_bindir}/RenderingCxxTests
%attr(755,root,root) %{_bindir}/VTKBenchMark
%attr(755,root,root) %{_bindir}/VolumeRenderingCxxTests
%attr(755,root,root) %{_bindir}/WidgetsCxxTests
%attr(755,root,root) %{_bindir}/SocketClient
%attr(755,root,root) %{_bindir}/SocketServer

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/HierarchicalBoxPipeline
%attr(755,root,root) %{_bindir}/MultiBlock
%attr(755,root,root) %{_bindir}/Arrays
%attr(755,root,root) %{_bindir}/Cube
%attr(755,root,root) %{_bindir}/RGrid
%attr(755,root,root) %{_bindir}/SGrid
%attr(755,root,root) %{_bindir}/Medical1
%attr(755,root,root) %{_bindir}/Medical2
%attr(755,root,root) %{_bindir}/Medical3
%attr(755,root,root) %{_bindir}/finance
%attr(755,root,root) %{_bindir}/AmbientSpheres
%attr(755,root,root) %{_bindir}/Cylinder
%attr(755,root,root) %{_bindir}/DiffuseSpheres
%attr(755,root,root) %{_bindir}/SpecularSpheres
%attr(755,root,root) %{_bindir}/Cone
%attr(755,root,root) %{_bindir}/Cone2
%attr(755,root,root) %{_bindir}/Cone3
%attr(755,root,root) %{_bindir}/Cone4
%attr(755,root,root) %{_bindir}/Cone5
%attr(755,root,root) %{_bindir}/Cone6
%{_examplesdir}/%{name}-%{version}

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/vtk-data
%{_datadir}/vtk-data/Baseline
%{_datadir}/vtk-data/Data
%{_datadir}/vtk-data/VTKData.readme
