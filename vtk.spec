# TODO:
# - handle VTK_USE_MPEG2_ENCODER (see CMakeLists.txt)
# - handle MPI and VTK_USE_PARALLEL_BGL (Parallel Boost Graph Library, BR: boost >= 1.40)
# - more system libraries? (check for VTK_THIRD_PARTY_SUBDIR in Utilities/CMakeLists.txt)
# - CUDA for Accelerators/Piston (on bcond)
# - NVCtrlLib for Rendering/OpenGL (on bcond)
# - VTK_USE_SYSTEM_XDMF2=ON ? (but our xdmf-devel seems not compatible)
# - python bcond?
# - use system exodusii
#
# Conditional build
%bcond_without	java		# Java wrappers
%bcond_without	ffmpeg		# FFMPEG .avi saving support
%bcond_without	doc		# doxygen documentation
%bcond_with	OSMesa		# build with OSMesa (https://bugzilla.redhat.com/show_bug.cgi?id=744434)
%bcond_with	system_gl2ps	# use system gl2ps (VTK currently is carrying local modifications to gl2ps, incl. gl2psTextOptColorBL function)
%bcond_with	system_fmt	# use system fmt (VTK currently is carrying local modifications to fmt)

%{?use_default_jdk}

%define		system_modules	doubleconversion eigen expat %{?with_system_fmt:fmt} freetype %{?with_system_gl2ps:gl2ps} glew hdf5 jpeg jsoncpp libharu libproj libxml2 lz4 lzma mpi4py netcdf ogg png pugixml sqlite theora tiff zfp zlib

Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl.UTF-8):	Zestaw narzędzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
Version:	9.3.1
Release:	8
License:	BSD
Group:		Libraries
#Source0Download: https://vtk.org/download/
Source0:	https://www.vtk.org/files/release/9.3/VTK-%{version}.tar.gz
# Source0-md5:	1b237485ca2eaaf676e2031a71e82d0d
Source1:	https://www.vtk.org/files/release/9.3/VTKData-%{version}.tar.gz
# Source1-md5:	29b3a39da48e43f0cd0ad7f0a84b9e9a
Patch0:		ffmpeg6.patch
URL:		https://vtk.org/
%{?with_OSMesa:BuildRequires: Mesa-libOSMesa-devel}
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Designer-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6OpenGL-devel
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Sql-devel
BuildRequires:	Qt6UiTools-devel
%ifarch %{x8664}
BuildRequires:	Qt6WebEngine-devel
%endif
BuildRequires:	Qt6Xml-devel
BuildRequires:	R
BuildRequires:	boost-devel >= 1.39
BuildRequires:	cmake >= 3.3
BuildRequires:	double-conversion-devel
%{?with_doc:BuildRequires:	doxygen}
BuildRequires:	eigen3 >= 2.91.0
BuildRequires:	expat-devel
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gdal-devel
%{?with_system_gl2ps:BuildRequires:	gl2ps-devel >= 1.4.0}
BuildRequires:	glew-devel
BuildRequires:	gnuplot
BuildRequires:	graphviz
BuildRequires:	hdf5-devel
%if %{with java}
%buildrequires_jdk
BuildRequires:	jpackage-utils
BuildRequires:	%{use_jdk}-jre-base-X11
%endif
BuildRequires:	jsoncpp-devel >= 0.7.0
%{?with_system_fmt:BuildRequires:	libfmt-devel >= 9.1.0}
BuildRequires:	libharu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	lz4-devel
BuildRequires:	motif-devel
BuildRequires:	mysql-devel
BuildRequires:	netcdf-cxx4-devel >= 4
# some code using it exists (Domains/Chemistry), but is not included in cmakefiles
#BuildRequires:	openqube-devel
BuildRequires:	perl-base
BuildRequires:	postgresql-devel
BuildRequires:	proj-devel >= 9.0
BuildRequires:	pugixml-devel
BuildRequires:	python3-devel
BuildRequires:	python3-PyQt6
BuildRequires:	qt6-build
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.021
BuildRequires:	sqlite3-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	unixODBC-devel
BuildRequires:	wget
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildConflicts:	libXNVCtrl-devel
Obsoletes:	vtk-tcl < 8.2.0-1
Obsoletes:	vtk-tcl-devel < 8.2.0-1
%{?with_system_gl2ps:Requires:	gl2ps >= 1.4.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	lib.*Python.*\.so.* libvtkWebCore\.so.*

%description
The Visualization ToolKit (VTK) is an object oriented software system
for 3D computer graphics, image processing, and visualization. VTK
includes a textbook, a C++ class library, and several interpreted
interface layers including Java, and Python. VTK supports a wide
variety of visualization algorithms including scalar, vector, tensor,
texture, and volumetric methods. It also supports advanced modeling
techniques like implicit modeling, polygon reduction, mesh smoothing,
cutting, contouring, and Delaunay triangulation. Moreover, dozens of
imaging algorithms have been integrated into the system. This allows
mixing 2D imaging / 3D graphics algorithms and data.

%description -l pl.UTF-8
Visualization TookKit (VTK) to obiektowo zorientowany system
oprogramowania do trójwymiarowej grafiki komputerowej, przetwarzania
obrazu i wizualizacji. VTK zawiera książkę, bibliotekę klas C++ oraz
kilka interpretowanych warstw interfejsów, w tym dla Javy i Pythona.
VTK obsługuje szeroki zakres algorytmów wizualizacji, w tym metody
skalarne, wektorowe, tensorowe, teksturowe i wolumetryczne. Obsługuje
także zaawansowane techniki modelowania, takie jak modelowanie
implicite, redukcja wielokątów, wygładzanie siatki, przycinanie,
konturowanie i triangulacja Delaunaya. Co więcej, wiele algorytmów
obrazowania zostało zintegrowanych z systemem. Pozwala to na mieszanie
algorytmów obrazowania 2D i grafiki 3D.

%package devel
Summary:	VTK header files for building C++ code
Summary(pl.UTF-8):	Pliki nagłówkowe VTK dla C++
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	double-conversion-devel
Requires:	glew-devel
Requires:	libstdc++-devel

%description devel
This provides the VTK header files required to compile C++ programs
that use VTK to do 3D visualisation.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki nagłówkowe VTK do kompilowania programów
C++ używających VTK do wizualizacji 3D.

%package qt
Summary:	Qt6 bindings and Qt6 Designer plugin for VTK
Summary(pl.UTF-8):	Wiązania Qt6 oraz wtyczka Qt6 Designera do VTK
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core
Requires:	Qt6Gui
Requires:	Qt6Network
Requires:	Qt6OpenGL
Requires:	Qt6Sql
%ifarch %{x8664}
Requires:	Qt6WebEngine
%endif

%description qt
Qt6 bindings and Qt6 Designer plugin for VTK.

%description qt -l pl.UTF-8
Wiązania Qt6 oraz wtyczka Qt6 Designera do VTK.

%package qt-devel
Summary:	Header files for VTK Qt6 bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Qt6 do VTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	Qt6Core-devel
Requires:	Qt6Gui-devel
Requires:	Qt6OpenGL-devel
Requires:	Qt6Sql-devel

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

%package python3
Summary:	Python 3 bindings for VTK
Summary(pl.UTF-8):	Wiązania Pythona 3 do VTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# or separate qt parts again?
Requires:	%{name}-qt = %{version}-%{release}
Obsoletes:	vtk-python < 8.2.0-1
Obsoletes:	vtk-python-qt < 6.0.0-1
Obsoletes:	vtk-python-sip < 6.0.0-1

%description python3
This package contains Python 3 bindings for VTK.

%description python3 -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona 3 do VTK.

%package python3-devel
Summary:	Header files for Python 3 VTK binding
Summary(pl.UTF-8):	Pliki nagłówkowe wiązania Pythona 3 do VTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-python3 = %{version}-%{release}
Requires:	python3-devel
Obsoletes:	vtk-python-devel < 8.2.0-1

%description python3-devel
Header files for Python 3 VTK binding.

%description python3-devel -l pl.UTF-8
Pliki nagłówkowe wiązania Pythona 3 do VTK.

%package examples
Summary:	C++ and Python example programs/scripts for VTK
Summary(pl.UTF-8):	Przykładowe programy/skrypty w C++ i Pythonie dla VTK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}

%description examples
This package contains all the examples from the VTK source. To compile
the C++ examples you will need to install the vtk-devel package as
well. The Python examples can be run with the corresponding packages
(vtk-python3).

%description examples -l pl.UTF-8
Ten pakiet zawiera wszystkie przykłady ze źródeł VTK. Do skompilowania
przykładów w C++ trzeba doinstalować pakiet vtk-devel. Przykłady w
Pythonie można uruchamiać przy użyciu odpowiednich pakietów
(vtk-python3).

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
BuildArch:	noarch

%description data
This package contains all the data from the VTKData repository. These
data are required to run various examples from the vtk-examples
package.

%description data -l pl.UTF-8
Ten pakiet zawiera wszystkie dane z repozytorium VTKData. Dane te są
potrzebne do uruchamiania różnych przykładów z pakietu vtk-examples.

%prep
%setup -q -n VTK-%{version} -b 1
%patch -P 0 -p1

# Replace relative path ../../../VTKData with destination filesystem path
grep -Erl '(\.\./)+VTKData' Examples | xargs \
	%{__perl} -pi -e 's,(\.\./)+VTKData,%{_datadir}/vtk-9.3,g'

# Save an unbuilt copy of the Example's sources for %doc
mkdir vtk-examples
cp -a Examples vtk-examples
find vtk-examples -type f | xargs chmod -R a-x

for x in %{system_modules}; do
%{__rm} -r ThirdParty/*/vtk$x
done

%{__mv} Wrapping/Tools/README{,-Wrapping}.md

%build
export CFLAGS="%{rpmcflags} -D_UNICODE -DHAVE_UINTPTR_T"
export CXXFLAGS="%{rpmcxxflags} -D_UNICODE -DHAVE_UINTPTR_T"
export CPPFLAGS="%{rpmcppflags}"
%if %{with java}
export JAVA_HOME=%{java_home}
%ifarch x32
# getting "java.lang.OutOfMemoryError: Java heap space" during the build
export JAVA_TOOL_OPTIONS=-Xmx2048m
%endif
%endif

# handle cmake & ccache
# http://stackoverflow.com/questions/1815688/how-to-use-ccache-with-cmake
# ASM fix: http://lists.busybox.net/pipermail/buildroot/2013-March/069436.html
if [[ "%{__cc}" = *ccache* ]]; then
	cc="%{__cc}"
	cxx="%{__cxx}"
	ccache="
	-DCMAKE_C_COMPILER="ccache" -DCMAKE_C_COMPILER_ARG1="${cc#ccache }" \
	-DCMAKE_CXX_COMPILER="ccache" -DCMAKE_CXX_COMPILER_ARG1="${cxx#ccache }" \
	"
else
	ccache="
	-DCMAKE_C_COMPILER="%{__cc}" \
	-DCMAKE_CXX_COMPILER="%{__cxx}" \
	"
fi

USE_EXTERNAL_MODULE=""
for x in %{system_modules}; do
	USE_EXTERNAL_MODULE="$USE_EXTERNAL_MODULE -DVTK_MODULE_USE_EXTERNAL_VTK_${x}:BOOL=ON"
done

mkdir -p build
cd build
%cmake .. \
	$ccache \
	-Wno-dev \
	%{cmake_on_off doc VTK_BUILD_DOCUMENTATION} \
	-DVTK_BUILD_EXAMPLES:BOOL=ON \
	-DVTK_BUILD_TESTING:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DOPENGL_INCLUDE_PATH:PATH=%{_includedir}/GL \
	-DVTK_CUSTOM_LIBRARY_SUFFIX="" \
	-DVTK_VERSIONED_INSTALL:BOOL=OFF \
	-DVTK_GROUP_ENABLE_Imaging:STRING=YES \
	-DVTK_GROUP_ENABLE_Qt:STRING=YES \
	-DVTK_GROUP_ENABLE_Rendering:STRING=YES \
	-DVTK_GROUP_ENABLE_StandAlone:STRING=YES \
	-DVTK_GROUP_ENABLE_Views:STRING=YES \
	-DVTK_GROUP_ENABLE_Web:STRING=YES \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
	-DCMAKE_INSTALL_INCLUDEDIR:PATH=include \
	-DCMAKE_INSTALL_BINDIR:PATH=bin \
	-DCMAKE_INSTALL_DATAROOTDIR:PATH=share \
	%{?with_OSMesa:-DVTK_OPENGL_HAS_OSMESA:BOOL=ON} \
	-DVTK_USE_EXTERNAL:BOOL=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_utf8:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_exprtk:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_fast_float:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_nlohmannjson:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_pegtl:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_cgns:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_ioss:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_verdict:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_cli11:BOOL=OFF \
	%{!?with_system_fmt:-DVTK_MODULE_USE_EXTERNAL_VTK_fmt:BOOL=OFF} \
	%{!?with_system_gl2ps:-DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps:BOOL=OFF} \
%if %{with ffmpeg}
	-DVTK_MODULE_ENABLE_VTK_IOFFMPEG:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_RenderingFFMPEGOpenGL2:STRING=YES \
%else
	-DVTK_MODULE_ENABLE_VTK_IOFFMPEG:STRING=NO \
%endif
%if %{with java}
	-DVTK_WRAP_JAVA:BOOL=ON \
	-DJAVA_INCLUDE_PATH:PATH=$JAVA_HOME/include \
	-DJAVA_INCLUDE_PATH2:PATH=$JAVA_HOME/include/linux \
	-DJAVA_AWT_INCLUDE_PATH:PATH=$JAVA_HOME/include \
%else
	-DVTK_WRAP_JAVA:BOOL=OFF \
%endif
	-DVTK_WRAP_PYTHON:BOOL=ON \
	-DVTK_PYTHON_VERSION=3

LD_LIBRARY_PATH="$(pwd)/%{_lib}:$LD_LIBRARY_PATH" \
%{__make}

%if %{with doc}
%{__make} DoxygenDoc
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/ld.so.conf.d,%{_examplesdir}/%{name}-%{version}}

LD_LIBRARY_PATH="$(pwd)/build/%{_lib}:$LD_LIBRARY_PATH" \
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

for f in $(cd build/ExternalData/Testing ; find Data -type l); do
	install -Dp build/ExternalData/Testing/$f $RPM_BUILD_ROOT%{_datadir}/vtk-9.3/$f
done

# Install test binaries
for f in build/bin/*Tests build/bin/Test*; do
	install $f $RPM_BUILD_ROOT%{_bindir}
done

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun qt -p /sbin/ldconfig

%post	java -p /sbin/ldconfig
%postun	java -p /sbin/ldconfig

%post	python3 -p /sbin/ldconfig
%postun	python3 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md vtkBanner.gif vtkLogo.ico Wrapping/Tools/README*
%doc %{_datadir}/licenses
%attr(755,root,root) %{_libdir}/libvtkChartsCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkChartsCore.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonColor.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonColor.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonComputationalGeometry.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonComputationalGeometry.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonCore.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonDataModel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonDataModel.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonExecutionModel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonExecutionModel.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonMath.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonMath.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonMisc.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonMisc.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonSystem.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonSystem.so.1
%attr(755,root,root) %{_libdir}/libvtkCommonTransforms.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonTransforms.so.1
%attr(755,root,root) %{_libdir}/libvtkDICOMParser.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkDICOMParser.so.1
%attr(755,root,root) %{_libdir}/libvtkDomainsChemistryOpenGL2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkDomainsChemistryOpenGL2.so.1
%attr(755,root,root) %{_libdir}/libvtkDomainsChemistry.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkDomainsChemistry.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersAMR.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersAMR.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersCellGrid.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersCellGrid.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersCore.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersExtraction.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersExtraction.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersFlowPaths.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersFlowPaths.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersGeneral.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersGeneral.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersGeneric.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersGeneric.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersGeometry.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersGeometry.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersGeometryPreview.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersGeometryPreview.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersHybrid.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersHybrid.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersHyperTree.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersHyperTree.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersImaging.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersImaging.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersModeling.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersModeling.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersParallel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersParallel.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersParallelImaging.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersParallelImaging.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersPoints.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersPoints.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersProgrammable.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersProgrammable.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersReduction.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersReduction.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersSMP.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersSMP.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersSelection.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersSelection.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersSources.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersSources.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersStatistics.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersStatistics.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersTensor.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersTensor.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersTexture.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersTexture.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersTopology.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersTopology.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersVerdict.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersVerdict.so.1
%attr(755,root,root) %{_libdir}/libvtkGeovisCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkGeovisCore.so.1
%attr(755,root,root) %{_libdir}/libvtkIOAMR.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOAMR.so.1
%attr(755,root,root) %{_libdir}/libvtkIOAsynchronous.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOAsynchronous.so.1
%attr(755,root,root) %{_libdir}/libvtkIOCellGrid.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOCellGrid.so.1
%attr(755,root,root) %{_libdir}/libvtkIOCityGML.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOCityGML.so.1
%attr(755,root,root) %{_libdir}/libvtkIOCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOCore.so.1
%attr(755,root,root) %{_libdir}/libvtkIOEnSight.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOEnSight.so.1
%attr(755,root,root) %{_libdir}/libvtkIOExodus.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOExodus.so.1
%attr(755,root,root) %{_libdir}/libvtkIOExport.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOExport.so.1
%attr(755,root,root) %{_libdir}/libvtkIOExportPDF.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOExportPDF.so.1
%if %{with ffmpeg}
%attr(755,root,root) %{_libdir}/libvtkIOFFMPEG.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOFFMPEG.so.1
%endif
%attr(755,root,root) %{_libdir}/libvtkIOFLUENTCFF.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOFLUENTCFF.so.1
%attr(755,root,root) %{_libdir}/libvtkIOGeometry.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOGeometry.so.1
%attr(755,root,root) %{_libdir}/libvtkIOImage.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOImage.so.1
%attr(755,root,root) %{_libdir}/libvtkIOImport.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOImport.so.1
%attr(755,root,root) %{_libdir}/libvtkIOInfovis.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOInfovis.so.1
%attr(755,root,root) %{_libdir}/libvtkIOLSDyna.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOLSDyna.so.1
%attr(755,root,root) %{_libdir}/libvtkIOLegacy.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOLegacy.so.1
%attr(755,root,root) %{_libdir}/libvtkIOMINC.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOMINC.so.1
%attr(755,root,root) %{_libdir}/libvtkIOMovie.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOMovie.so.1
%attr(755,root,root) %{_libdir}/libvtkIONetCDF.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIONetCDF.so.1
%attr(755,root,root) %{_libdir}/libvtkIOPLY.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOPLY.so.1
%attr(755,root,root) %{_libdir}/libvtkIOParallel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOParallel.so.1
%attr(755,root,root) %{_libdir}/libvtkIOParallelExodus.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOParallelExodus.so.1
%attr(755,root,root) %{_libdir}/libvtkIOParallelXML.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOParallelXML.so.1
%attr(755,root,root) %{_libdir}/libvtkIOSQL.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOSQL.so.1
%attr(755,root,root) %{_libdir}/libvtkIOSegY.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOSegY.so.1
%attr(755,root,root) %{_libdir}/libvtkIOTecplotTable.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOTecplotTable.so.1
%attr(755,root,root) %{_libdir}/libvtkIOVeraOut.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOVeraOut.so.1
%attr(755,root,root) %{_libdir}/libvtkIOVideo.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOVideo.so.1
%attr(755,root,root) %{_libdir}/libvtkIOXML.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOXML.so.1
%attr(755,root,root) %{_libdir}/libvtkIOXMLParser.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOXMLParser.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingColor.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingColor.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingCore.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingFourier.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingFourier.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingGeneral.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingGeneral.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingHybrid.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingHybrid.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingMath.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingMath.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingMorphological.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingMorphological.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingSources.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingSources.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingStatistics.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingStatistics.so.1
%attr(755,root,root) %{_libdir}/libvtkImagingStencil.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkImagingStencil.so.1
%attr(755,root,root) %{_libdir}/libvtkInfovisCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkInfovisCore.so.1
%attr(755,root,root) %{_libdir}/libvtkInfovisLayout.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkInfovisLayout.so.1
%attr(755,root,root) %{_libdir}/libvtkInteractionImage.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkInteractionImage.so.1
%attr(755,root,root) %{_libdir}/libvtkInteractionStyle.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkInteractionStyle.so.1
%attr(755,root,root) %{_libdir}/libvtkInteractionWidgets.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkInteractionWidgets.so.1
%attr(755,root,root) %{_libdir}/libvtkParallelCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkParallelCore.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingAnnotation.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingAnnotation.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingCellGrid.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingCellGrid.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingContext2D.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingContext2D.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingContextOpenGL2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingContextOpenGL2.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingCore.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingFreeType.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingFreeType.so.1
%if %{with ffmpeg}
%attr(755,root,root) %{_libdir}/libvtkRenderingFFMPEGOpenGL2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingFFMPEGOpenGL2.so.1
%endif
%attr(755,root,root) %{_libdir}/libvtkRenderingGL2PSOpenGL2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingGL2PSOpenGL2.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingImage.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingImage.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingLabel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingLabel.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingLOD.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingLOD.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingOpenGL2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingOpenGL2.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingParallel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingParallel.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingVolumeOpenGL2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingVolumeOpenGL2.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingVolume.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingVolume.so.1
%attr(755,root,root) %{_libdir}/libvtkTestingGenericBridge.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkTestingGenericBridge.so.1
%attr(755,root,root) %{_libdir}/libvtkTestingIOSQL.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkTestingIOSQL.so.1
%attr(755,root,root) %{_libdir}/libvtkTestingRendering.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkTestingRendering.so.1
%attr(755,root,root) %{_libdir}/libvtkViewsContext2D.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkViewsContext2D.so.1
%attr(755,root,root) %{_libdir}/libvtkViewsCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkViewsCore.so.1
%attr(755,root,root) %{_libdir}/libvtkViewsInfovis.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkViewsInfovis.so.1
%attr(755,root,root) %{_libdir}/libvtkexodusII.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkexodusII.so.1
%attr(755,root,root) %{_libdir}/libvtkgl2ps.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkgl2ps.so.1
%attr(755,root,root) %{_libdir}/libvtkmetaio.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkmetaio.so.1
%attr(755,root,root) %{_libdir}/libvtksys.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtksys.so.1
%attr(755,root,root) %{_libdir}/libvtkverdict.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkverdict.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersParallelDIY2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersParallelDIY2.so.1
%attr(755,root,root) %{_libdir}/libvtkIOCGNSReader.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOCGNSReader.so.1
%attr(755,root,root) %{_libdir}/libvtkIOCONVERGECFD.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOCONVERGECFD.so.1
%attr(755,root,root) %{_libdir}/libvtkIOCesium3DTiles.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOCesium3DTiles.so.1
%attr(755,root,root) %{_libdir}/libvtkIOChemistry.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOChemistry.so.1
%attr(755,root,root) %{_libdir}/libvtkIOExportGL2PS.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOExportGL2PS.so.1
%attr(755,root,root) %{_libdir}/libvtkIOHDF.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOHDF.so.1
%attr(755,root,root) %{_libdir}/libvtkIOIOSS.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOIOSS.so.1
%attr(755,root,root) %{_libdir}/libvtkIOMotionFX.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOMotionFX.so.1
%attr(755,root,root) %{_libdir}/libvtkIOOggTheora.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkIOOggTheora.so.1
%attr(755,root,root) %{_libdir}/libvtkParallelDIY.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkParallelDIY.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingHyperTreeGrid.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingHyperTreeGrid.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingLICOpenGL2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingLICOpenGL2.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingSceneGraph.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingSceneGraph.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingUI.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingUI.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingVtkJS.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingVtkJS.so.1
%attr(755,root,root) %{_libdir}/libvtkTestingDataModel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkTestingDataModel.so.1
%attr(755,root,root) %{_libdir}/libvtkWrappingTools.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkWrappingTools.so.1
%attr(755,root,root) %{_libdir}/libvtkcgns.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkcgns.so.1
%attr(755,root,root) %{_libdir}/libvtkfmt.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkfmt.so.1
%attr(755,root,root) %{_libdir}/libvtkioss.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkioss.so.1
%attr(755,root,root) %{_libdir}/libvtkkissfft.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkkissfft.so.1
%attr(755,root,root) %{_libdir}/libvtkloguru.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkloguru.so.1

%{_libdir}/libvtkWebCore.so.*.*
%ghost %{_libdir}/libvtkWebCore.so.1
%{_libdir}/libvtkWebGLExporter.so.*.*
%ghost %{_libdir}/libvtkWebGLExporter.so.1

%files devel
%defattr(644,root,root,755)
%doc Utilities/Upgrading/*
%{?with_doc:%doc %{_docdir}/vtk}
%attr(755,root,root) %{_bindir}/vtkProbeOpenGLVersion
%attr(755,root,root) %{_bindir}/vtkWrapHierarchy
%attr(755,root,root) %{_libdir}/libvtkChartsCore.so
%attr(755,root,root) %{_libdir}/libvtkCommonColor.so
%attr(755,root,root) %{_libdir}/libvtkCommonComputationalGeometry.so
%attr(755,root,root) %{_libdir}/libvtkCommonCore.so
%attr(755,root,root) %{_libdir}/libvtkCommonDataModel.so
%attr(755,root,root) %{_libdir}/libvtkCommonExecutionModel.so
%attr(755,root,root) %{_libdir}/libvtkCommonMath.so
%attr(755,root,root) %{_libdir}/libvtkCommonMisc.so
%attr(755,root,root) %{_libdir}/libvtkCommonSystem.so
%attr(755,root,root) %{_libdir}/libvtkCommonTransforms.so
%attr(755,root,root) %{_libdir}/libvtkDICOMParser.so
%attr(755,root,root) %{_libdir}/libvtkDomainsChemistryOpenGL2.so
%attr(755,root,root) %{_libdir}/libvtkDomainsChemistry.so
%attr(755,root,root) %{_libdir}/libvtkFiltersAMR.so
%attr(755,root,root) %{_libdir}/libvtkFiltersCellGrid.so
%attr(755,root,root) %{_libdir}/libvtkFiltersCore.so
%attr(755,root,root) %{_libdir}/libvtkFiltersExtraction.so
%attr(755,root,root) %{_libdir}/libvtkFiltersFlowPaths.so
%attr(755,root,root) %{_libdir}/libvtkFiltersGeneral.so
%attr(755,root,root) %{_libdir}/libvtkFiltersGeneric.so
%attr(755,root,root) %{_libdir}/libvtkFiltersGeometry.so
%attr(755,root,root) %{_libdir}/libvtkFiltersGeometryPreview.so
%attr(755,root,root) %{_libdir}/libvtkFiltersHybrid.so
%attr(755,root,root) %{_libdir}/libvtkFiltersHyperTree.so
%attr(755,root,root) %{_libdir}/libvtkFiltersImaging.so
%attr(755,root,root) %{_libdir}/libvtkFiltersModeling.so
%attr(755,root,root) %{_libdir}/libvtkFiltersParallelDIY2.so
%attr(755,root,root) %{_libdir}/libvtkFiltersParallelImaging.so
%attr(755,root,root) %{_libdir}/libvtkFiltersParallel.so
%attr(755,root,root) %{_libdir}/libvtkFiltersPoints.so
%attr(755,root,root) %{_libdir}/libvtkFiltersProgrammable.so
%attr(755,root,root) %{_libdir}/libvtkFiltersReduction.so
%attr(755,root,root) %{_libdir}/libvtkFiltersSelection.so
%attr(755,root,root) %{_libdir}/libvtkFiltersSMP.so
%attr(755,root,root) %{_libdir}/libvtkFiltersSources.so
%attr(755,root,root) %{_libdir}/libvtkFiltersStatistics.so
%attr(755,root,root) %{_libdir}/libvtkFiltersTensor.so
%attr(755,root,root) %{_libdir}/libvtkFiltersTexture.so
%attr(755,root,root) %{_libdir}/libvtkFiltersTopology.so
%attr(755,root,root) %{_libdir}/libvtkFiltersVerdict.so
%attr(755,root,root) %{_libdir}/libvtkGeovisCore.so
%attr(755,root,root) %{_libdir}/libvtkImagingColor.so
%attr(755,root,root) %{_libdir}/libvtkImagingCore.so
%attr(755,root,root) %{_libdir}/libvtkImagingFourier.so
%attr(755,root,root) %{_libdir}/libvtkImagingGeneral.so
%attr(755,root,root) %{_libdir}/libvtkImagingHybrid.so
%attr(755,root,root) %{_libdir}/libvtkImagingMath.so
%attr(755,root,root) %{_libdir}/libvtkImagingMorphological.so
%attr(755,root,root) %{_libdir}/libvtkImagingSources.so
%attr(755,root,root) %{_libdir}/libvtkImagingStatistics.so
%attr(755,root,root) %{_libdir}/libvtkImagingStencil.so
%attr(755,root,root) %{_libdir}/libvtkInfovisCore.so
%attr(755,root,root) %{_libdir}/libvtkInfovisLayout.so
%attr(755,root,root) %{_libdir}/libvtkInteractionImage.so
%attr(755,root,root) %{_libdir}/libvtkInteractionStyle.so
%attr(755,root,root) %{_libdir}/libvtkInteractionWidgets.so
%attr(755,root,root) %{_libdir}/libvtkIOAMR.so
%attr(755,root,root) %{_libdir}/libvtkIOAsynchronous.so
%attr(755,root,root) %{_libdir}/libvtkIOCellGrid.so
%attr(755,root,root) %{_libdir}/libvtkIOCesium3DTiles.so
%attr(755,root,root) %{_libdir}/libvtkIOCGNSReader.so
%attr(755,root,root) %{_libdir}/libvtkIOChemistry.so
%attr(755,root,root) %{_libdir}/libvtkIOCityGML.so
%attr(755,root,root) %{_libdir}/libvtkIOCONVERGECFD.so
%attr(755,root,root) %{_libdir}/libvtkIOCore.so
%attr(755,root,root) %{_libdir}/libvtkIOEnSight.so
%attr(755,root,root) %{_libdir}/libvtkIOExodus.so
%attr(755,root,root) %{_libdir}/libvtkIOExportGL2PS.so
%attr(755,root,root) %{_libdir}/libvtkIOExportPDF.so
%attr(755,root,root) %{_libdir}/libvtkIOExport.so
%{?with_ffmpeg:%attr(755,root,root) %{_libdir}/libvtkIOFFMPEG.so}
%attr(755,root,root) %{_libdir}/libvtkIOFLUENTCFF.so
%attr(755,root,root) %{_libdir}/libvtkIOGeometry.so
%attr(755,root,root) %{_libdir}/libvtkIOHDF.so
%attr(755,root,root) %{_libdir}/libvtkIOImage.so
%attr(755,root,root) %{_libdir}/libvtkIOImport.so
%attr(755,root,root) %{_libdir}/libvtkIOInfovis.so
%attr(755,root,root) %{_libdir}/libvtkIOIOSS.so
%attr(755,root,root) %{_libdir}/libvtkIOLegacy.so
%attr(755,root,root) %{_libdir}/libvtkIOLSDyna.so
%attr(755,root,root) %{_libdir}/libvtkIOMINC.so
%attr(755,root,root) %{_libdir}/libvtkIOMotionFX.so
%attr(755,root,root) %{_libdir}/libvtkIOMovie.so
%attr(755,root,root) %{_libdir}/libvtkIONetCDF.so
%attr(755,root,root) %{_libdir}/libvtkIOOggTheora.so
%attr(755,root,root) %{_libdir}/libvtkIOParallelExodus.so
%attr(755,root,root) %{_libdir}/libvtkIOParallel.so
%attr(755,root,root) %{_libdir}/libvtkIOParallelXML.so
%attr(755,root,root) %{_libdir}/libvtkIOPLY.so
%attr(755,root,root) %{_libdir}/libvtkIOSegY.so
%attr(755,root,root) %{_libdir}/libvtkIOSQL.so
%attr(755,root,root) %{_libdir}/libvtkIOTecplotTable.so
%attr(755,root,root) %{_libdir}/libvtkIOVeraOut.so
%attr(755,root,root) %{_libdir}/libvtkIOVideo.so
%attr(755,root,root) %{_libdir}/libvtkIOXMLParser.so
%attr(755,root,root) %{_libdir}/libvtkIOXML.so
%attr(755,root,root) %{_libdir}/libvtkParallelCore.so
%attr(755,root,root) %{_libdir}/libvtkParallelDIY.so
%attr(755,root,root) %{_libdir}/libvtkRenderingAnnotation.so
%attr(755,root,root) %{_libdir}/libvtkRenderingCellGrid.so
%attr(755,root,root) %{_libdir}/libvtkRenderingContext2D.so
%attr(755,root,root) %{_libdir}/libvtkRenderingContextOpenGL2.so
%attr(755,root,root) %{_libdir}/libvtkRenderingCore.so
%attr(755,root,root) %{_libdir}/libvtkRenderingFreeType.so
%{?with_ffmpeg:%attr(755,root,root) %{_libdir}/libvtkRenderingFFMPEGOpenGL2.so}
%attr(755,root,root) %{_libdir}/libvtkRenderingGL2PSOpenGL2.so
%attr(755,root,root) %{_libdir}/libvtkRenderingHyperTreeGrid.so
%attr(755,root,root) %{_libdir}/libvtkRenderingImage.so
%attr(755,root,root) %{_libdir}/libvtkRenderingLabel.so
%attr(755,root,root) %{_libdir}/libvtkRenderingLICOpenGL2.so
%attr(755,root,root) %{_libdir}/libvtkRenderingLOD.so
%attr(755,root,root) %{_libdir}/libvtkRenderingOpenGL2.so
%attr(755,root,root) %{_libdir}/libvtkRenderingParallel.so
%attr(755,root,root) %{_libdir}/libvtkRenderingSceneGraph.so
%attr(755,root,root) %{_libdir}/libvtkRenderingUI.so
%attr(755,root,root) %{_libdir}/libvtkRenderingVolumeOpenGL2.so
%attr(755,root,root) %{_libdir}/libvtkRenderingVolume.so
%attr(755,root,root) %{_libdir}/libvtkRenderingVtkJS.so
%attr(755,root,root) %{_libdir}/libvtkTestingDataModel.so
%attr(755,root,root) %{_libdir}/libvtkTestingGenericBridge.so
%attr(755,root,root) %{_libdir}/libvtkTestingIOSQL.so
%attr(755,root,root) %{_libdir}/libvtkTestingRendering.so
%attr(755,root,root) %{_libdir}/libvtkViewsContext2D.so
%attr(755,root,root) %{_libdir}/libvtkViewsCore.so
%attr(755,root,root) %{_libdir}/libvtkViewsInfovis.so
%attr(755,root,root) %{_libdir}/libvtkWebCore.so
%attr(755,root,root) %{_libdir}/libvtkWebGLExporter.so
%attr(755,root,root) %{_libdir}/libvtkWrappingTools.so
%attr(755,root,root) %{_libdir}/libvtkcgns.so
%attr(755,root,root) %{_libdir}/libvtkexodusII.so
%attr(755,root,root) %{_libdir}/libvtkfmt.so
%attr(755,root,root) %{_libdir}/libvtkgl2ps.so
%attr(755,root,root) %{_libdir}/libvtkioss.so
%attr(755,root,root) %{_libdir}/libvtkkissfft.so
%attr(755,root,root) %{_libdir}/libvtkloguru.so
%attr(755,root,root) %{_libdir}/libvtkmetaio.so
%attr(755,root,root) %{_libdir}/libvtksys.so
%attr(755,root,root) %{_libdir}/libvtkverdict.so
%dir %{_includedir}/vtk
%{_includedir}/vtk/DICOM*.h
%{_includedir}/vtk/DatabaseSchemaWith2Tables.h
%{_includedir}/vtk/LSDyna*.h
%{_includedir}/vtk/vtkexodusII
%{_includedir}/vtk/vtkgl2ps
%{_includedir}/vtk/vtkkwiml
%{_includedir}/vtk/vtkmetaio
%{_includedir}/vtk/vtksys
%{_includedir}/vtk/vtk*.h
%{_includedir}/vtk/vtk*.txx
%{_includedir}/vtk/SMP
%{_includedir}/vtk/VerdictVector.hpp
%{_includedir}/vtk/octree
%{_includedir}/vtk/verdict.h
%{_includedir}/vtk/verdict_defines.hpp
%{_includedir}/vtk/vtkMathPrivate.hxx
%{_includedir}/vtk/vtkcgns
%{_includedir}/vtk/vtkcli11
%{_includedir}/vtk/vtkdiy2
%{_includedir}/vtk/vtkexprtk
%{_includedir}/vtk/vtkfast_float
%{_includedir}/vtk/vtkfmt
%{_includedir}/vtk/vtkkissfft
%{_includedir}/vtk/vtkloguru
%{_includedir}/vtk/vtknlohmannjson
%{_includedir}/vtk/vtkutf8
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/hierarchy

%if %{with java}
%exclude %{_includedir}/vtk/vtkJava*.h
%endif
%exclude %{_includedir}/vtk/vtkPython*.h
%{_libdir}/cmake/vtk

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtkGUISupportQt.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkGUISupportQt.so.1
%attr(755,root,root) %{_libdir}/libvtkGUISupportQtQuick.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkGUISupportQtQuick.so.1
%attr(755,root,root) %{_libdir}/libvtkGUISupportQtSQL.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkGUISupportQtSQL.so.1
%attr(755,root,root) %{_libdir}/libvtkRenderingQt.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkRenderingQt.so.1
%attr(755,root,root) %{_libdir}/libvtkViewsQt.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkViewsQt.so.1
%dir %{_libdir}/qml/VTK.9.3
%{_libdir}/qml/VTK.9.3/plugins.qmltypes
%attr(755,root,root) %{_libdir}/qml/VTK.9.3/libqmlvtkplugin.so
%{_libdir}/qml/VTK.9.3/qmldir

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtkGUISupportQt.so
%attr(755,root,root) %{_libdir}/libvtkGUISupportQtQuick.so
%attr(755,root,root) %{_libdir}/libvtkGUISupportQtSQL.so
%attr(755,root,root) %{_libdir}/libvtkRenderingQt.so
%attr(755,root,root) %{_libdir}/libvtkViewsQt.so
%{_includedir}/vtk/QFilterTreeProxyModel.h
%{_includedir}/vtk/QQuickVTKInteractiveWidget.h
%{_includedir}/vtk/QQuickVTKInteractorAdapter.h
%{_includedir}/vtk/QQuickVTKItem.h
%{_includedir}/vtk/QQuickVTKRenderItem.h
%{_includedir}/vtk/QQuickVTKRenderWindow.h
%{_includedir}/vtk/QVTKApplication.h
%{_includedir}/vtk/QVTKInteractor.h
%{_includedir}/vtk/QVTKInteractorAdapter.h
%{_includedir}/vtk/QVTKOpenGLNativeWidget.h
%{_includedir}/vtk/QVTKOpenGLStereoWidget.h
%{_includedir}/vtk/QVTKOpenGLWindow.h
%{_includedir}/vtk/QVTKRenderWidget.h
%{_includedir}/vtk/QVTKRenderWindowAdapter.h
%{_includedir}/vtk/QVTKTableModelAdapter.h
%{_includedir}/vtk/QVTKWin32Header.h

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vtkParseJava
%attr(755,root,root) %{_bindir}/vtkWrapJava
# common library
%attr(755,root,root) %{_libdir}/libvtkJava.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkJava.so.1
# java modules
%dir %{_libdir}/java/vtk-*
%attr(755,root,root) %{_libdir}/java/vtk-*/libvtk*Java.so
%{_libdir}/java/vtk.jar

%files java-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtkJava.so
%exclude %{_includedir}/vtk/vtkJava*.h
%endif

%files python3
%defattr(644,root,root,755)
%doc Wrapping/Python/README*
%attr(755,root,root) %{_bindir}/vtkWrapPython
%attr(755,root,root) %{_bindir}/vtkWrapPythonInit
%attr(755,root,root) %{_bindir}/vtkpython
%attr(755,root,root) %{_libdir}/libvtkCommonPython.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkCommonPython.so.1
%attr(755,root,root) %{_libdir}/libvtkFiltersPython.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkFiltersPython.so.1
%attr(755,root,root) %{_libdir}/libvtkPythonContext2D.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkPythonContext2D.so.1
%attr(755,root,root) %{_libdir}/libvtkPythonInterpreter.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkPythonInterpreter.so.1
%attr(755,root,root) %{_libdir}/libvtkWrappingPythonCore3*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvtkWrappingPythonCore3*.so.1
%{py3_sitedir}/__pycache__/*
%{py3_sitedir}/vtk.py
%dir %{py3_sitedir}/vtkmodules
%{py3_sitedir}/vtkmodules/*.py
%{py3_sitedir}/vtkmodules/__pycache__
%dir %{py3_sitedir}/vtkmodules/gtk
%{py3_sitedir}/vtkmodules/gtk/*.py
%{py3_sitedir}/vtkmodules/gtk/__pycache__
%dir %{py3_sitedir}/vtkmodules/numpy_interface
%{py3_sitedir}/vtkmodules/numpy_interface/*.py
%{py3_sitedir}/vtkmodules/numpy_interface/__pycache__
%dir %{py3_sitedir}/vtkmodules/qt
%{py3_sitedir}/vtkmodules/qt/*.py
%{py3_sitedir}/vtkmodules/qt/__pycache__
%dir %{py3_sitedir}/vtkmodules/test
%{py3_sitedir}/vtkmodules/test/*.py
%{py3_sitedir}/vtkmodules/test/__pycache__
%dir %{py3_sitedir}/vtkmodules/tk
%{py3_sitedir}/vtkmodules/tk/__pycache__
%{py3_sitedir}/vtkmodules/tk/*.py
%dir %{py3_sitedir}/vtkmodules/util
%{py3_sitedir}/vtkmodules/util/*.py
%{py3_sitedir}/vtkmodules/util/__pycache__
%dir %{py3_sitedir}/vtkmodules/web
%{py3_sitedir}/vtkmodules/web/*.py
%{py3_sitedir}/vtkmodules/web/__pycache__
%dir %{py3_sitedir}/vtkmodules/wx
%{py3_sitedir}/vtkmodules/wx/*.py
%{py3_sitedir}/vtkmodules/wx/__pycache__
%attr(755,root,root) %{py3_sitedir}/vtkmodules/vtk*.so

%files python3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtkCommonPython.so
%attr(755,root,root) %{_libdir}/libvtkFiltersPython.so
%attr(755,root,root) %{_libdir}/libvtkPythonContext2D.so
%attr(755,root,root) %{_libdir}/libvtkPythonInterpreter.so
%attr(755,root,root) %{_libdir}/libvtkWrappingPythonCore3*.so
%{_includedir}/vtk/PyVTK*.h
%{_includedir}/vtk/vtkPython*.h
%{_includedir}/vtk/vtkpythonmodules

%files test-suite
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*Tests
%attr(755,root,root) %{_bindir}/Test*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/vtk-9.3
%{_datadir}/vtk-9.3/Data
