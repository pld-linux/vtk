# TODO:
# - handle VTK_USE_MPEG2_ENCODER (see CMakeLists.txt)
# - handle MPI and VTK_USE_PARALLEL_BGL (Parallel Boost Graph Library, BR: boost >= 1.40)
# - more system libraries? (check for VTK_THIRD_PARTY_SUBDIR in Utilities/CMakeLists.txt)
# - CUDA for Accelerators/Piston (on bcond)
# - NVCtrlLib for Rendering/OpenGL (on bcond)
# - IO/GDAL? (seems not handled by main build system)
# - IO/ODBC? (VTK_USE_ODBC=ON)
# - Xdmf2? (not build by default?)
#
# Conditional build
%bcond_without	java		# Java wrappers
%bcond_without	ffmpeg		# FFMPEG .avi saving support
%bcond_with	OSMesa		# build with OSMesa (https://bugzilla.redhat.com/show_bug.cgi?id=744434)
%bcond_with	system_proj	# use system PROJ.4 (needs 4.3 with exposed internals, not ready for 4.4+)
#
Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl.UTF-8):	Zestaw narzędzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
Version:	6.0.0
Release:	3
License:	BSD
Group:		Libraries
Source0:	http://www.vtk.org/files/release/6.0/%{name}-%{version}.tar.gz
# Source0-md5:	72ede4812c90bdc55172702f0cad02bb
Source1:	http://www.vtk.org/files/release/6.0/%{name}data-%{version}.tar.gz
# Source1-md5:	f40bcfe92439575ae56aa3f2fcd30149
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-install.patch
Patch2:		%{name}-chemistry.patch
URL:		http://www.vtk.org/
%{?with_OSMesa:BuildRequires: Mesa-libOSMesa-devel}
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-devel
BuildRequires:	QtCore-devel >= 4.5.0
BuildRequires:	QtGui-devel >= 4.5.0
BuildRequires:	QtNetwork-devel >= 4.5.0
BuildRequires:	QtOpenGL-devel >= 4.5.0
BuildRequires:	QtSql-devel >= 4.5.0
BuildRequires:	QtWebKit-devel >= 4.5.0
BuildRequires:	QtXmlPatterns-devel >= 4.5.0
BuildRequires:	R
BuildRequires:	boost-devel >= 1.39
BuildRequires:	cmake >= 2.8.5
BuildRequires:	doxygen
BuildRequires:	eigen >= 2
BuildRequires:	expat-devel
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gl2ps-devel >= 1.3.8
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
BuildRequires:	motif-devel
BuildRequires:	mysql-devel
BuildRequires:	openqube-devel
BuildRequires:	postgresql-devel
%{?with_system_proj:BuildRequires:	proj-devel >= 4.3, proj-devel < 4.4}
BuildRequires:	python-devel
BuildRequires:	python-sip-devel
BuildRequires:	python-PyQt4-devel
BuildRequires:	qt4-build >= 4.5.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sip
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	wget
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
Requires:	gl2ps >= 1.3.8
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
Summary:	Qt bindings and Qt Designer plugin for VTK
Summary(pl.UTF-8):	Wiązania Qt oraz wtyczka Qt Designera do VTK
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore >= 4.5.0
Requires:	QtGui >= 4.5.0
Requires:	QtNetwork >= 4.5.0
Requires:	QtOpenGL >= 4.5.0
Requires:	QtSql >= 4.5.0
Requires:	QtWebKit >= 4.5.0

%description qt
Qt bindings and Qt Designer plugin for VTK.

%description qt -l pl.UTF-8
Wiązania Qt oraz wtyczka Qt Designera do VTK.

%package qt-devel
Summary:	Header files for VTK Qt bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Qt do VTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	QtCore-devel >= 4.5.0
Requires:	QtGui-devel >= 4.5.0
Requires:	QtOpenGL-devel >= 4.5.0
Requires:	QtSql-devel >= 4.5.0

%description qt-devel
Header files for VTK Qt bindings.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe wiązań Qt do VTK.

%package java
Summary:	Java bindings for VTK
Summary(pl.UTF-8):	Wiązania Javy do VTK
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
# or separate qt parts?
Requires:	%{name}-qt = %{version}-%{release}

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
# or separate qt parts again?
Requires:	%{name}-qt = %{version}-%{release}
Obsoletes:	vtk-python-qt < 6.0.0-1
Obsoletes:	vtk-python-sip < 6.0.0-1

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

%package tcl
Summary:	Tcl bindings for VTK
Summary(pl.UTF-8):	Wiązania języka Tcl do VTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# or separate qt parts?
Requires:	%{name}-qt = %{version}-%{release}

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
	-DVTK_CUSTOM_LIBRARY_SUFFIX="" \
	-DVTK_INSTALL_ARCHIVE_DIR:PATH=%{_lib}/vtk \
	-DVTK_INSTALL_INCLUDE_DIR:PATH=include/vtk \
	-DVTK_INSTALL_LIBRARY_DIR:PATH=%{_lib}/vtk \
	-DVTK_INSTALL_PACKAGE_DIR:PATH=%{_lib}/cmake/vtk \
	-DVTK_INSTALL_TCL_DIR:PATH=share/tcl%{tcl_version}/vtk \
	-DVTK_INSTALL_QT_DIR=/%{_lib}/qt4/plugins/designer \
	%{?with_OSMesa:-DVTK_OPENGL_HAS_OSMESA:BOOL=ON} \
	-DVTK_WRAP_PYTHON:BOOL=ON \
	-DVTK_PYTHON_SETUP_ARGS="--prefix=/usr --root=$RPM_BUILD_ROOT" \
	-DVTK_USE_SYSTEM_LIBRARIES:BOOL=ON \
	-DVTK_USE_OGGTHEORA_ENCODER:BOOL=ON \
	-DVTK_USE_RENDERING:BOOL=ON \
	-DVTK_USE_SYSTEM_HDF5:BOOL=ON \
	%{!?with_system_proj:-DVTK_USE_SYSTEM_LIBPROJ4:BOOL=OFF} \
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
	-DVTK_WRAP_TCL:BOOL=ON \
	-DVTK_Group_Imaging:BOOL=ON \
	-DVTK_Group_Qt:BOOL=ON \
	-DVTK_Group_Rendering:BOOL=ON \
	-DVTK_Group_StandAlone:BOOL=ON \
	-DVTK_Group_Tk:BOOL=ON \
	-DVTK_Group_Views:BOOL=ON \
	-DModule_vtkFiltersStatisticsGnuR:BOOL=ON

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

cp -a VTKDATA%{version}/* $RPM_BUILD_ROOT%{_datadir}/vtk-data
cp -a vtk-examples/Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# Install utilities
install build/bin/lproj $RPM_BUILD_ROOT%{_bindir}

# Install examples
for f in \
AmbientSpheres \
Arrays \
BalloonWidget \
BandedContours \
Cone \
Cone2 \
Cone3 \
Cone4 \
Cone5 \
Cone6 \
Cube \
Cylinder \
Delaunay3D \
Delaunay3DAlpha \
DiffuseSpheres \
DumpXMLFile \
FilledContours \
FixedPointVolumeRayCastMapperCT \
GPURenderDemo \
Generate2DAMRDataSetWithPulse \
Generate3DAMRDataSetWithPulse \
GenerateCubesFromLabels \
GenerateModelsFromLabels \
HierarchicalBoxPipeline \
ImageDataLIC2DDemo \
ImageSlicing \
LabeledMesh \
MaterialObjects \
Medical1 \
Medical2 \
Medical3 \
MultiBlock \
ParticleReader \
RGrid \
SGrid \
Slider \
Slider2D \
SpecularSpheres \
StructuredGridLIC2DDemo \
SurfaceLICDemo \
TimeRenderer \
TimeRenderer2 \
TubesWithVaryingRadiusAndColors \
finance ; do
	install build/bin/$f $RPM_BUILD_ROOT%{_bindir}
done

# Install test binaries
for f in build/bin/*Tests build/bin/Test* build/bin/VTKBenchMark ; do
	install $f $RPM_BUILD_ROOT%{_bindir}
done

install build/bin/VTKJavaExecutable $RPM_BUILD_ROOT%{_bindir}
install build/bin/vtkpython $RPM_BUILD_ROOT%{_bindir}

# unwanted doxygen files and misplaced verdict docs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/vtk-6.0/{doxygen,verdict}

# only *.pyc are built by default, add *.pyo
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/vtk
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun qt -p /sbin/ldconfig

%post	java -p /sbin/ldconfig
%postun	java -p /sbin/ldconfig

%post	python -p /sbin/ldconfig
%postun	python -p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html vtkLogo.jpg vtkBanner.gif Wrapping/Tools/README*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ld.so.conf.d/vtk-%{_arch}.conf
%dir %{_libdir}/vtk
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistry.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFilters*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIO*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInteraction*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkLocalExample.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF_cxx.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingAnnotation.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContext2D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeType.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeTypeOpenGL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingGL2PS.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingHybridOpenGL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingImage.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLOD.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLabel.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingOpenGL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolume.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeAMR.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeOpenGL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkTesting*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovis.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovis.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkalglib.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkexoIIc.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkftgl.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkjsoncpp.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkproj4.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtksqlite.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so.1
%exclude %{_libdir}/vtk/libvtk*Java.so.1
%exclude %{_libdir}/vtk/libvtk*Python2?D.so.1
%exclude %{_libdir}/vtk/libvtkWrappingPython2?Core.so.1
%exclude %{_libdir}/vtk/libvtk*TCL.so.1

%files devel
%defattr(644,root,root,755)
%doc Utilities/Upgrading/*
%attr(755,root,root) %{_bindir}/lproj
%attr(755,root,root) %{_bindir}/vtkEncodeString
%attr(755,root,root) %{_bindir}/vtkHashSource
%attr(755,root,root) %{_bindir}/vtkParseOGLExt
%attr(755,root,root) %{_bindir}/vtkProcessShader
%attr(755,root,root) %{_bindir}/vtkWrapHierarchy
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistry.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFilters*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIO*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteraction*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkLocalExample.so
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF.so
%attr(755,root,root) %{_libdir}/vtk/libvtkNetCDF_cxx.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingAnnotation.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContext2D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeType.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeTypeOpenGL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingGL2PS.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingHybridOpenGL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingImage.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLOD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLabel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingOpenGL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolume.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeAMR.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeOpenGL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkTesting*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkalglib.so
%attr(755,root,root) %{_libdir}/vtk/libvtkexoIIc.so
%attr(755,root,root) %{_libdir}/vtk/libvtkftgl.so
%attr(755,root,root) %{_libdir}/vtk/libvtkjsoncpp.so
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so
%attr(755,root,root) %{_libdir}/vtk/libvtkproj4.so
%attr(755,root,root) %{_libdir}/vtk/libvtksqlite.so
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so
%exclude %{_libdir}/vtk/libvtk*Java.so
%exclude %{_libdir}/vtk/libvtk*Python2?D.so
%exclude %{_libdir}/vtk/libvtkWrappingPython2?Core.so
%exclude %{_libdir}/vtk/libvtk*TCL.so
%{_libdir}/vtk/libvtkWrappingTools.a
%dir %{_includedir}/vtk
%{_includedir}/vtk/DICOM*.h
%{_includedir}/vtk/DatabaseSchemaWith2Tables.h
%{_includedir}/vtk/JSONCPP
%{_includedir}/vtk/LSDyna*.h
%{_includedir}/vtk/alglib
%{_includedir}/vtk/vtklibproj4
%{_includedir}/vtk/vtkmetaio
%{_includedir}/vtk/vtknetcdf
%{_includedir}/vtk/vtkverdict
%{_includedir}/vtk/vtksqlite
%{_includedir}/vtk/vtksys
%{_includedir}/vtk/vtk*.h
%{_includedir}/vtk/vtk*.txx
%exclude %{_includedir}/vtk/vtkEventQtSlotConnect.h
%exclude %{_includedir}/vtk/vtkGUISupportQt*.h
%exclude %{_includedir}/vtk/vtkJavaUtil.h
%exclude %{_includedir}/vtk/vtkWrappingJavaModule.h
%exclude %{_includedir}/vtk/vtkPython*.h
%exclude %{_includedir}/vtk/vtkQImageToImageSource.h
%exclude %{_includedir}/vtk/vtkQt*.h
%exclude %{_includedir}/vtk/vtkRenderingQtModule.h
%exclude %{_includedir}/vtk/vtkTcl*.h
%exclude %{_includedir}/vtk/vtkTk*.h
%exclude %{_includedir}/vtk/vtkViewsQtModule.h
%{_libdir}/cmake/vtk

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQt.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQtOpenGL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQtSQL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQtWebkit.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingQt.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsQt.so.1
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libQVTKWidgetPlugin.so

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQt.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQtOpenGL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQtSQL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQtWebkit.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingQt.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsQt.so
%{_includedir}/vtk/QFilterTreeProxyModel.h
%{_includedir}/vtk/QVTK*.h
%{_includedir}/vtk/vtkEventQtSlotConnect.h
%{_includedir}/vtk/vtkGUISupportQt*.h
%{_includedir}/vtk/vtkQImageToImageSource.h
%{_includedir}/vtk/vtkQt*.h
%{_includedir}/vtk/vtkRenderingQtModule.h
%{_includedir}/vtk/vtkViewsQtModule.h

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/VTKJavaExecutable
%attr(755,root,root) %{_bindir}/vtkParseJava
%attr(755,root,root) %{_bindir}/vtkWrapJava
# common library
%attr(755,root,root) %{_libdir}/vtk/libvtkWrappingJava.so.1
# java modules
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon*Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFilters*Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIO*Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging*Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis*Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteraction*Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkLocalExampleJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRendering*Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingRenderingJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViews*Java.so
%{_libdir}/vtk/vtk.jar

%files java-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkWrappingJava.so
%{_includedir}/vtk/vtkJavaUtil.h
%{_includedir}/vtk/vtkWrappingJavaModule.h
%endif

%files python
%defattr(644,root,root,755)
%doc Wrapping/Python/README*
%attr(755,root,root) %{_bindir}/vtkWrapPython
%attr(755,root,root) %{_bindir}/vtkWrapPythonInit
%attr(755,root,root) %{_bindir}/vtkpython
%attr(755,root,root) %{_libdir}/vtk/libvtk*Python2?D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingPythonTkWidgets-6.0.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWrappingPython2?Core.so.1
%dir %{py_sitedir}/vtk
%{py_sitedir}/vtk/*.py[co]
%dir %{py_sitedir}/vtk/gtk
%{py_sitedir}/vtk/gtk/*.py[co]
%dir %{py_sitedir}/vtk/qt4
%{py_sitedir}/vtk/qt4/*.py[co]
%dir %{py_sitedir}/vtk/test
%{py_sitedir}/vtk/test/*.py[co]
%dir %{py_sitedir}/vtk/tk
%{py_sitedir}/vtk/tk/*.py[co]
%dir %{py_sitedir}/vtk/util
%{py_sitedir}/vtk/util/*.py[co]
%dir %{py_sitedir}/vtk/wx
%{py_sitedir}/vtk/wx/*.py[co]
%attr(755,root,root) %{py_sitedir}/vtk/vtk*Python.so
%{py_sitedir}/VTK-*-py*.egg-info

%files python-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtk*Python2?D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWrappingPython2?Core.so
%{_includedir}/vtk/PyVTK*.h
%{_includedir}/vtk/vtkPython*.h

%files tcl
%defattr(644,root,root,755)
%doc Wrapping/Tcl/README*
%attr(755,root,root) %{_bindir}/vtkWrapTcl
%attr(755,root,root) %{_bindir}/vtkWrapTclInit
%attr(755,root,root) %{_bindir}/vtk
%{_datadir}/tcl8.5/vtk
%attr(755,root,root) %{_libdir}/vtk/libvtk*TCL.so.1

%files tcl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtk*TCL.so
%{_includedir}/vtk/vtkTcl*.h
%{_includedir}/vtk/vtkTk*.h

%files test-suite
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*Tests
%attr(755,root,root) %{_bindir}/Test*
%attr(755,root,root) %{_bindir}/VTKBenchMark

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
%attr(755,root,root) %{_bindir}/BalloonWidget
%attr(755,root,root) %{_bindir}/BandedContours
%attr(755,root,root) %{_bindir}/Delaunay3D
%attr(755,root,root) %{_bindir}/Delaunay3DAlpha
%attr(755,root,root) %{_bindir}/DumpXMLFile
%attr(755,root,root) %{_bindir}/FilledContours
%attr(755,root,root) %{_bindir}/FixedPointVolumeRayCastMapperCT
%attr(755,root,root) %{_bindir}/GPURenderDemo
%attr(755,root,root) %{_bindir}/Generate2DAMRDataSetWithPulse
%attr(755,root,root) %{_bindir}/Generate3DAMRDataSetWithPulse
%attr(755,root,root) %{_bindir}/GenerateCubesFromLabels
%attr(755,root,root) %{_bindir}/GenerateModelsFromLabels
%attr(755,root,root) %{_bindir}/ImageDataLIC2DDemo
%attr(755,root,root) %{_bindir}/ImageSlicing
%attr(755,root,root) %{_bindir}/LabeledMesh
%attr(755,root,root) %{_bindir}/MaterialObjects
%attr(755,root,root) %{_bindir}/ParticleReader
%attr(755,root,root) %{_bindir}/Slider
%attr(755,root,root) %{_bindir}/Slider2D
%attr(755,root,root) %{_bindir}/StructuredGridLIC2DDemo
%attr(755,root,root) %{_bindir}/SurfaceLICDemo
%attr(755,root,root) %{_bindir}/TimeRenderer
%attr(755,root,root) %{_bindir}/TimeRenderer2
%attr(755,root,root) %{_bindir}/TubesWithVaryingRadiusAndColors
%{_examplesdir}/%{name}-%{version}

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/vtk-data
%{_datadir}/vtk-data/Baseline
%{_datadir}/vtk-data/Copyright.txt
%{_datadir}/vtk-data/Data
%{_datadir}/vtk-data/VERSION
%{_datadir}/vtk-data/VTKData.readme
