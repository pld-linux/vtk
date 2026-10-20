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

%define		system_modules	eigen expat %{?with_system_fmt:fmt} freetype %{?with_system_gl2ps:gl2ps} hdf5 jpeg jsoncpp libharu libproj libxml2 lz4 lzma mpi4py netcdf ogg png pugixml sqlite theora tiff zlib

Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl.UTF-8):	Zestaw narzędzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
%define	vtk_base_version 9.7
Version:	%{vtk_base_version}.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://vtk.org/download/
Source0:	https://www.vtk.org/files/release/%{vtk_base_version}/VTK-%{version}.tar.gz
# Source0-md5:	9426290b94f8f49afff3df83e5ee7749
Source1:	https://www.vtk.org/files/release/%{vtk_base_version}/VTKData-%{version}.tar.gz
# Source1-md5:	18e3b5dfb00c9df6fbbcf61e48932c50
URL:		https://vtk.org/
%{?with_OSMesa:BuildRequires: Mesa-libOSMesa-devel}
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Designer-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6OpenGL-devel
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Qml-devel >= 6.9.2-5
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Sql-devel
BuildRequires:	Qt6TaskTree-devel
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
%{?buildrequires_jre_x11}
BuildRequires:	jpackage-utils
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
BuildRequires:	python3-PyQt6
BuildRequires:	python3-devel
BuildRequires:	qt6-build
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.062
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
# vtk-config.cmake runs find_package() on these for the modules named (via VTK's third-party wrappers)
# RenderingOpenGL2, GUISupportQt
Requires:	OpenGL-devel
# IOCore
Requires:	double-conversion-devel
# FiltersStatistics
Requires:	eigen3 >= 2.91.0
# IOXMLParser
Requires:	expat-devel
# RenderingFreeType
Requires:	freetype-devel >= 2
# RenderingOpenGL2 (via glew)
Requires:	glew-devel
# IOAMR, IOCGNSReader, hdf5 module
Requires:	hdf5-devel
# IOImage
Requires:	libjpeg-devel
# IOImage
Requires:	libpng-devel
Requires:	libstdc++-devel
# IOImage
Requires:	libtiff-devel
# IOCore
Requires:	lz4-devel
# CommonDataModel, IOImage
Requires:	pugixml-devel
# RenderingOpenGL2, RenderingUI
Requires:	xorg-lib-libX11-devel
# IOCore (lzma)
Requires:	xz-devel
# IOCore, IOImage, IOGeometry
Requires:	zlib-devel

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

# Replace relative path ../../../VTKData with destination filesystem path
grep -Erl '(\.\./)+VTKData' Examples | xargs \
	%{__perl} -pi -e 's,(\.\./)+VTKData,%{_datadir}/vtk-%{vtk_base_version},g'

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
	-DVTK_CUSTOM_LIBRARY_VERSION="%{vtk_base_version}" \
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
	-DVTK_MODULE_USE_EXTERNAL_VTK_scn:BOOL=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_token:BOOL=OFF \
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
	install -Dp build/ExternalData/Testing/$f $RPM_BUILD_ROOT%{_datadir}/vtk-%{vtk_base_version}/$f
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
%{_libdir}/libvtkChartsCore.so.*.*
%ghost %{_libdir}/libvtkChartsCore.so.1
%{_libdir}/libvtkCommonCache.so.9.7
%ghost %{_libdir}/libvtkCommonCache.so.1
%{_libdir}/libvtkCommonColor.so.*.*
%ghost %{_libdir}/libvtkCommonColor.so.1
%{_libdir}/libvtkCommonComputationalGeometry.so.*.*
%ghost %{_libdir}/libvtkCommonComputationalGeometry.so.1
%{_libdir}/libvtkCommonCore.so.*.*
%ghost %{_libdir}/libvtkCommonCore.so.1
%{_libdir}/libvtkCommonDataModel.so.*.*
%ghost %{_libdir}/libvtkCommonDataModel.so.1
%{_libdir}/libvtkCommonExecutionModel.so.*.*
%ghost %{_libdir}/libvtkCommonExecutionModel.so.1
%{_libdir}/libvtkCommonMath.so.*.*
%ghost %{_libdir}/libvtkCommonMath.so.1
%{_libdir}/libvtkCommonMisc.so.*.*
%ghost %{_libdir}/libvtkCommonMisc.so.1
%{_libdir}/libvtkCommonSystem.so.*.*
%ghost %{_libdir}/libvtkCommonSystem.so.1
%{_libdir}/libvtkCommonTransforms.so.*.*
%ghost %{_libdir}/libvtkCommonTransforms.so.1
%{_libdir}/libvtkDICOMParser.so.*.*
%ghost %{_libdir}/libvtkDICOMParser.so.1
%{_libdir}/libvtkDomainsChemistryOpenGL2.so.*.*
%ghost %{_libdir}/libvtkDomainsChemistryOpenGL2.so.1
%{_libdir}/libvtkDomainsChemistry.so.*.*
%ghost %{_libdir}/libvtkDomainsChemistry.so.1
%{_libdir}/libvtkFiltersAMR.so.*.*
%ghost %{_libdir}/libvtkFiltersAMR.so.1
%{_libdir}/libvtkFiltersCellGrid.so.*.*
%ghost %{_libdir}/libvtkFiltersCellGrid.so.1
%{_libdir}/libvtkFiltersCore.so.*.*
%ghost %{_libdir}/libvtkFiltersCore.so.1
%{_libdir}/libvtkFiltersExtraction.so.*.*
%ghost %{_libdir}/libvtkFiltersExtraction.so.1
%{_libdir}/libvtkFiltersFlowPaths.so.*.*
%ghost %{_libdir}/libvtkFiltersFlowPaths.so.1
%{_libdir}/libvtkFiltersGeneral.so.*.*
%ghost %{_libdir}/libvtkFiltersGeneral.so.1
%{_libdir}/libvtkFiltersGeneric.so.*.*
%ghost %{_libdir}/libvtkFiltersGeneric.so.1
%{_libdir}/libvtkFiltersGeometry.so.*.*
%ghost %{_libdir}/libvtkFiltersGeometry.so.1
%{_libdir}/libvtkFiltersGeometryPreview.so.*.*
%ghost %{_libdir}/libvtkFiltersGeometryPreview.so.1
%{_libdir}/libvtkFiltersHybrid.so.*.*
%ghost %{_libdir}/libvtkFiltersHybrid.so.1
%{_libdir}/libvtkFiltersHyperTree.so.*.*
%ghost %{_libdir}/libvtkFiltersHyperTree.so.1
%{_libdir}/libvtkFiltersImaging.so.*.*
%ghost %{_libdir}/libvtkFiltersImaging.so.1
%{_libdir}/libvtkFiltersMeshing.so.9.7
%ghost %{_libdir}/libvtkFiltersMeshing.so.1
%{_libdir}/libvtkFiltersModeling.so.*.*
%ghost %{_libdir}/libvtkFiltersModeling.so.1
%{_libdir}/libvtkFiltersParallel.so.*.*
%ghost %{_libdir}/libvtkFiltersParallel.so.1
%{_libdir}/libvtkFiltersParallelImaging.so.*.*
%ghost %{_libdir}/libvtkFiltersParallelImaging.so.1
%{_libdir}/libvtkFiltersPoints.so.*.*
%ghost %{_libdir}/libvtkFiltersPoints.so.1
%{_libdir}/libvtkFiltersProgrammable.so.*.*
%ghost %{_libdir}/libvtkFiltersProgrammable.so.1
%{_libdir}/libvtkFiltersReduction.so.*.*
%ghost %{_libdir}/libvtkFiltersReduction.so.1
%{_libdir}/libvtkFiltersSMP.so.*.*
%ghost %{_libdir}/libvtkFiltersSMP.so.1
%{_libdir}/libvtkFiltersSelection.so.*.*
%ghost %{_libdir}/libvtkFiltersSelection.so.1
%{_libdir}/libvtkFiltersSources.so.*.*
%ghost %{_libdir}/libvtkFiltersSources.so.1
%{_libdir}/libvtkFiltersStatistics.so.*.*
%ghost %{_libdir}/libvtkFiltersStatistics.so.1
%{_libdir}/libvtkFiltersTemporal.so.9.7
%ghost %{_libdir}/libvtkFiltersTemporal.so.1
%{_libdir}/libvtkFiltersTensor.so.*.*
%ghost %{_libdir}/libvtkFiltersTensor.so.1
%{_libdir}/libvtkFiltersTexture.so.*.*
%ghost %{_libdir}/libvtkFiltersTexture.so.1
%{_libdir}/libvtkFiltersTopology.so.*.*
%ghost %{_libdir}/libvtkFiltersTopology.so.1
%{_libdir}/libvtkFiltersVerdict.so.*.*
%ghost %{_libdir}/libvtkFiltersVerdict.so.1
%{_libdir}/libvtkGeovisCore.so.*.*
%ghost %{_libdir}/libvtkGeovisCore.so.1
%{_libdir}/libvtkIOAMR.so.*.*
%ghost %{_libdir}/libvtkIOAMR.so.1
%{_libdir}/libvtkIOAsynchronous.so.*.*
%ghost %{_libdir}/libvtkIOAsynchronous.so.1
%{_libdir}/libvtkIOAvmesh.so.9.7
%ghost %{_libdir}/libvtkIOAvmesh.so.1
%{_libdir}/libvtkIOCellGrid.so.*.*
%ghost %{_libdir}/libvtkIOCellGrid.so.1
%{_libdir}/libvtkIOCityGML.so.*.*
%ghost %{_libdir}/libvtkIOCityGML.so.1
%{_libdir}/libvtkIOCore.so.*.*
%ghost %{_libdir}/libvtkIOCore.so.1
%{_libdir}/libvtkIOERF.so.9.7
%ghost %{_libdir}/libvtkIOERF.so.1
%{_libdir}/libvtkIOEngys.so.9.7
%ghost %{_libdir}/libvtkIOEngys.so.1
%{_libdir}/libvtkIOFDS.so.9.7
%ghost %{_libdir}/libvtkIOFDS.so.1
%{_libdir}/libvtkIOLANLX3D.so.9.7
%ghost %{_libdir}/libvtkIOLANLX3D.so.1
%{_libdir}/libvtkIOEnSight.so.*.*
%ghost %{_libdir}/libvtkIOEnSight.so.1
%{_libdir}/libvtkIOExodus.so.*.*
%ghost %{_libdir}/libvtkIOExodus.so.1
%{_libdir}/libvtkIOExport.so.*.*
%ghost %{_libdir}/libvtkIOExport.so.1
%{_libdir}/libvtkIOExportPDF.so.*.*
%ghost %{_libdir}/libvtkIOExportPDF.so.1
%if %{with ffmpeg}
%{_libdir}/libvtkIOFFMPEG.so.*.*
%ghost %{_libdir}/libvtkIOFFMPEG.so.1
%endif
%{_libdir}/libvtkIOFLUENTCFF.so.*.*
%ghost %{_libdir}/libvtkIOFLUENTCFF.so.1
%{_libdir}/libvtkIOGeometry.so.*.*
%ghost %{_libdir}/libvtkIOGeometry.so.1
%{_libdir}/libvtkIOImage.so.*.*
%ghost %{_libdir}/libvtkIOImage.so.1
%{_libdir}/libvtkIOImport.so.*.*
%ghost %{_libdir}/libvtkIOImport.so.1
%{_libdir}/libvtkIOInfovis.so.*.*
%ghost %{_libdir}/libvtkIOInfovis.so.1
%{_libdir}/libvtkIOLSDyna.so.*.*
%ghost %{_libdir}/libvtkIOLSDyna.so.1
%{_libdir}/libvtkIOLegacy.so.*.*
%ghost %{_libdir}/libvtkIOLegacy.so.1
%{_libdir}/libvtkIOMINC.so.*.*
%ghost %{_libdir}/libvtkIOMINC.so.1
%{_libdir}/libvtkIOMovie.so.*.*
%ghost %{_libdir}/libvtkIOMovie.so.1
%{_libdir}/libvtkIONetCDF.so.*.*
%ghost %{_libdir}/libvtkIONetCDF.so.1
%{_libdir}/libvtkIOPLY.so.*.*
%ghost %{_libdir}/libvtkIOPLY.so.1
%{_libdir}/libvtkIOParallel.so.*.*
%ghost %{_libdir}/libvtkIOParallel.so.1
%{_libdir}/libvtkIOParallelExodus.so.*.*
%ghost %{_libdir}/libvtkIOParallelExodus.so.1
%{_libdir}/libvtkIOParallelXML.so.*.*
%ghost %{_libdir}/libvtkIOParallelXML.so.1
%{_libdir}/libvtkIOSQL.so.*.*
%ghost %{_libdir}/libvtkIOSQL.so.1
%{_libdir}/libvtkIOSegY.so.*.*
%ghost %{_libdir}/libvtkIOSegY.so.1
%{_libdir}/libvtkIOTecplotTable.so.*.*
%ghost %{_libdir}/libvtkIOTecplotTable.so.1
%{_libdir}/libvtkIOVeraOut.so.*.*
%ghost %{_libdir}/libvtkIOVeraOut.so.1
%{_libdir}/libvtkIOVideo.so.*.*
%ghost %{_libdir}/libvtkIOVideo.so.1
%{_libdir}/libvtkIOXML.so.*.*
%ghost %{_libdir}/libvtkIOXML.so.1
%{_libdir}/libvtkIOXMLParser.so.*.*
%ghost %{_libdir}/libvtkIOXMLParser.so.1
%{_libdir}/libvtkImagingColor.so.*.*
%ghost %{_libdir}/libvtkImagingColor.so.1
%{_libdir}/libvtkImagingCore.so.*.*
%ghost %{_libdir}/libvtkImagingCore.so.1
%{_libdir}/libvtkImagingFourier.so.*.*
%ghost %{_libdir}/libvtkImagingFourier.so.1
%{_libdir}/libvtkImagingGeneral.so.*.*
%ghost %{_libdir}/libvtkImagingGeneral.so.1
%{_libdir}/libvtkImagingHybrid.so.*.*
%ghost %{_libdir}/libvtkImagingHybrid.so.1
%{_libdir}/libvtkImagingMath.so.*.*
%ghost %{_libdir}/libvtkImagingMath.so.1
%{_libdir}/libvtkImagingMorphological.so.*.*
%ghost %{_libdir}/libvtkImagingMorphological.so.1
%{_libdir}/libvtkImagingSources.so.*.*
%ghost %{_libdir}/libvtkImagingSources.so.1
%{_libdir}/libvtkImagingStatistics.so.*.*
%ghost %{_libdir}/libvtkImagingStatistics.so.1
%{_libdir}/libvtkImagingStencil.so.*.*
%ghost %{_libdir}/libvtkImagingStencil.so.1
%{_libdir}/libvtkInfovisCore.so.*.*
%ghost %{_libdir}/libvtkInfovisCore.so.1
%{_libdir}/libvtkInfovisLayout.so.*.*
%ghost %{_libdir}/libvtkInfovisLayout.so.1
%{_libdir}/libvtkInteractionImage.so.*.*
%ghost %{_libdir}/libvtkInteractionImage.so.1
%{_libdir}/libvtkInteractionStyle.so.*.*
%ghost %{_libdir}/libvtkInteractionStyle.so.1
%{_libdir}/libvtkInteractionWidgets.so.*.*
%ghost %{_libdir}/libvtkInteractionWidgets.so.1
%{_libdir}/libvtkParallelCore.so.*.*
%ghost %{_libdir}/libvtkParallelCore.so.1
%{_libdir}/libvtkRenderingAnnotation.so.*.*
%ghost %{_libdir}/libvtkRenderingAnnotation.so.1
%{_libdir}/libvtkRenderingCellGrid.so.*.*
%ghost %{_libdir}/libvtkRenderingCellGrid.so.1
%{_libdir}/libvtkRenderingContext2D.so.*.*
%ghost %{_libdir}/libvtkRenderingContext2D.so.1
%{_libdir}/libvtkRenderingContextOpenGL2.so.*.*
%ghost %{_libdir}/libvtkRenderingContextOpenGL2.so.1
%{_libdir}/libvtkRenderingCore.so.*.*
%ghost %{_libdir}/libvtkRenderingCore.so.1
%{_libdir}/libvtkRenderingFreeType.so.*.*
%ghost %{_libdir}/libvtkRenderingFreeType.so.1
%if %{with ffmpeg}
%{_libdir}/libvtkRenderingFFMPEGOpenGL2.so.*.*
%ghost %{_libdir}/libvtkRenderingFFMPEGOpenGL2.so.1
%endif
%{_libdir}/libvtkRenderingGL2PSOpenGL2.so.*.*
%ghost %{_libdir}/libvtkRenderingGL2PSOpenGL2.so.1
%{_libdir}/libvtkRenderingImage.so.*.*
%ghost %{_libdir}/libvtkRenderingImage.so.1
%{_libdir}/libvtkRenderingLabel.so.*.*
%ghost %{_libdir}/libvtkRenderingLabel.so.1
%{_libdir}/libvtkRenderingLOD.so.*.*
%ghost %{_libdir}/libvtkRenderingLOD.so.1
%{_libdir}/libvtkRenderingOpenGL2.so.*.*
%ghost %{_libdir}/libvtkRenderingOpenGL2.so.1
%{_libdir}/libvtkRenderingParallel.so.*.*
%ghost %{_libdir}/libvtkRenderingParallel.so.1
%{_libdir}/libvtkRenderingVolumeOpenGL2.so.*.*
%ghost %{_libdir}/libvtkRenderingVolumeOpenGL2.so.1
%{_libdir}/libvtkRenderingVolume.so.*.*
%ghost %{_libdir}/libvtkRenderingVolume.so.1
%{_libdir}/libvtkRenderingGridAxes.so.9.7
%ghost %{_libdir}/libvtkRenderingGridAxes.so.1
%{_libdir}/libvtkRenderingVRModels.so.9.7
%ghost %{_libdir}/libvtkRenderingVRModels.so.1
%{_libdir}/libvtkTestingCore.so.9.7
%ghost %{_libdir}/libvtkTestingCore.so.1
%{_libdir}/libvtkTestingGenericBridge.so.*.*
%ghost %{_libdir}/libvtkTestingGenericBridge.so.1
%{_libdir}/libvtkTestingIOSQL.so.*.*
%ghost %{_libdir}/libvtkTestingIOSQL.so.1
%{_libdir}/libvtkTestingRendering.so.*.*
%ghost %{_libdir}/libvtkTestingRendering.so.1
%{_libdir}/libvtkViewsContext2D.so.*.*
%ghost %{_libdir}/libvtkViewsContext2D.so.1
%{_libdir}/libvtkViewsCore.so.*.*
%ghost %{_libdir}/libvtkViewsCore.so.1
%{_libdir}/libvtkViewsInfovis.so.*.*
%ghost %{_libdir}/libvtkViewsInfovis.so.1
%{_libdir}/libvtkexodusII.so.*.*
%ghost %{_libdir}/libvtkexodusII.so.1
%{_libdir}/libvtkgl2ps.so.*.*
%ghost %{_libdir}/libvtkgl2ps.so.1
%{_libdir}/libvtkmetaio.so.*.*
%ghost %{_libdir}/libvtkmetaio.so.1
%{_libdir}/libvtksys.so.*.*
%ghost %{_libdir}/libvtksys.so.1
%{_libdir}/libvtkverdict.so.*.*
%ghost %{_libdir}/libvtkverdict.so.1
%{_libdir}/libvtkFiltersParallelDIY2.so.*.*
%ghost %{_libdir}/libvtkFiltersParallelDIY2.so.1
%{_libdir}/libvtkIOCGNSReader.so.*.*
%ghost %{_libdir}/libvtkIOCGNSReader.so.1
%{_libdir}/libvtkIOCONVERGECFD.so.*.*
%ghost %{_libdir}/libvtkIOCONVERGECFD.so.1
%{_libdir}/libvtkIOCesium3DTiles.so.*.*
%ghost %{_libdir}/libvtkIOCesium3DTiles.so.1
%{_libdir}/libvtkIOChemistry.so.*.*
%ghost %{_libdir}/libvtkIOChemistry.so.1
%{_libdir}/libvtkIOExportGL2PS.so.*.*
%ghost %{_libdir}/libvtkIOExportGL2PS.so.1
%{_libdir}/libvtkIOHDF.so.*.*
%ghost %{_libdir}/libvtkIOHDF.so.1
%{_libdir}/libvtkIOIOSS.so.*.*
%ghost %{_libdir}/libvtkIOIOSS.so.1
%{_libdir}/libvtkIOMotionFX.so.*.*
%ghost %{_libdir}/libvtkIOMotionFX.so.1
%{_libdir}/libvtkIOOggTheora.so.*.*
%ghost %{_libdir}/libvtkIOOggTheora.so.1
%{_libdir}/libvtkParallelDIY.so.*.*
%ghost %{_libdir}/libvtkParallelDIY.so.1
%{_libdir}/libvtkRenderingHyperTreeGrid.so.*.*
%ghost %{_libdir}/libvtkRenderingHyperTreeGrid.so.1
%{_libdir}/libvtkRenderingLICOpenGL2.so.*.*
%ghost %{_libdir}/libvtkRenderingLICOpenGL2.so.1
%{_libdir}/libvtkRenderingSceneGraph.so.*.*
%ghost %{_libdir}/libvtkRenderingSceneGraph.so.1
%{_libdir}/libvtkRenderingUI.so.*.*
%ghost %{_libdir}/libvtkRenderingUI.so.1
%{_libdir}/libvtkRenderingVtkJS.so.*.*
%ghost %{_libdir}/libvtkRenderingVtkJS.so.1
%{_libdir}/libvtkTestingDataModel.so.*.*
%ghost %{_libdir}/libvtkTestingDataModel.so.1
%{_libdir}/libvtkWrappingTools.so.*.*
%ghost %{_libdir}/libvtkWrappingTools.so.1
%{_libdir}/libvtkcgns.so.*.*
%ghost %{_libdir}/libvtkcgns.so.1
%{_libdir}/libvtkfmt.so.*.*
%ghost %{_libdir}/libvtkfmt.so.1
%{_libdir}/libvtkioss.so.*.*
%ghost %{_libdir}/libvtkioss.so.1
%{_libdir}/libvtkkissfft.so.*.*
%ghost %{_libdir}/libvtkkissfft.so.1
%{_libdir}/libvtkloguru.so.*.*
%ghost %{_libdir}/libvtkloguru.so.1
%{_libdir}/libvtkglad.so.9.7
%ghost %{_libdir}/libvtkglad.so.1
%{_libdir}/libvtkscn.so.9.7
%ghost %{_libdir}/libvtkscn.so.1
%{_libdir}/libvtktoken.so.9.7
%ghost %{_libdir}/libvtktoken.so.1
%{_libdir}/libvtkx11.so.9.7
%ghost %{_libdir}/libvtkx11.so.1

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
%attr(755,root,root) %{_bindir}/vtkWrapJavaScript
%attr(755,root,root) %{_bindir}/vtkWrapSerDes
%{_libdir}/libvtkChartsCore.so
%{_libdir}/libvtkCommonColor.so
%{_libdir}/libvtkCommonComputationalGeometry.so
%{_libdir}/libvtkCommonCore.so
%{_libdir}/libvtkCommonDataModel.so
%{_libdir}/libvtkCommonExecutionModel.so
%{_libdir}/libvtkCommonMath.so
%{_libdir}/libvtkCommonMisc.so
%{_libdir}/libvtkCommonSystem.so
%{_libdir}/libvtkCommonTransforms.so
%{_libdir}/libvtkDICOMParser.so
%{_libdir}/libvtkDomainsChemistryOpenGL2.so
%{_libdir}/libvtkDomainsChemistry.so
%{_libdir}/libvtkFiltersAMR.so
%{_libdir}/libvtkFiltersCellGrid.so
%{_libdir}/libvtkFiltersCore.so
%{_libdir}/libvtkFiltersExtraction.so
%{_libdir}/libvtkFiltersFlowPaths.so
%{_libdir}/libvtkFiltersGeneral.so
%{_libdir}/libvtkFiltersGeneric.so
%{_libdir}/libvtkFiltersGeometry.so
%{_libdir}/libvtkFiltersGeometryPreview.so
%{_libdir}/libvtkFiltersHybrid.so
%{_libdir}/libvtkFiltersHyperTree.so
%{_libdir}/libvtkFiltersImaging.so
%{_libdir}/libvtkFiltersModeling.so
%{_libdir}/libvtkFiltersParallelDIY2.so
%{_libdir}/libvtkFiltersParallelImaging.so
%{_libdir}/libvtkFiltersParallel.so
%{_libdir}/libvtkFiltersPoints.so
%{_libdir}/libvtkFiltersProgrammable.so
%{_libdir}/libvtkFiltersReduction.so
%{_libdir}/libvtkFiltersSelection.so
%{_libdir}/libvtkFiltersSMP.so
%{_libdir}/libvtkFiltersSources.so
%{_libdir}/libvtkFiltersStatistics.so
%{_libdir}/libvtkFiltersTensor.so
%{_libdir}/libvtkFiltersTexture.so
%{_libdir}/libvtkFiltersTopology.so
%{_libdir}/libvtkFiltersVerdict.so
%{_libdir}/libvtkGeovisCore.so
%{_libdir}/libvtkImagingColor.so
%{_libdir}/libvtkImagingCore.so
%{_libdir}/libvtkImagingFourier.so
%{_libdir}/libvtkImagingGeneral.so
%{_libdir}/libvtkImagingHybrid.so
%{_libdir}/libvtkImagingMath.so
%{_libdir}/libvtkImagingMorphological.so
%{_libdir}/libvtkImagingSources.so
%{_libdir}/libvtkImagingStatistics.so
%{_libdir}/libvtkImagingStencil.so
%{_libdir}/libvtkInfovisCore.so
%{_libdir}/libvtkInfovisLayout.so
%{_libdir}/libvtkInteractionImage.so
%{_libdir}/libvtkInteractionStyle.so
%{_libdir}/libvtkInteractionWidgets.so
%{_libdir}/libvtkIOAMR.so
%{_libdir}/libvtkIOAsynchronous.so
%{_libdir}/libvtkIOCellGrid.so
%{_libdir}/libvtkIOCesium3DTiles.so
%{_libdir}/libvtkIOCGNSReader.so
%{_libdir}/libvtkIOChemistry.so
%{_libdir}/libvtkIOCityGML.so
%{_libdir}/libvtkIOCONVERGECFD.so
%{_libdir}/libvtkIOCore.so
%{_libdir}/libvtkIOEnSight.so
%{_libdir}/libvtkIOExodus.so
%{_libdir}/libvtkIOExportGL2PS.so
%{_libdir}/libvtkIOExportPDF.so
%{_libdir}/libvtkIOExport.so
%{?with_ffmpeg:%{_libdir}/libvtkIOFFMPEG.so}
%{_libdir}/libvtkIOFLUENTCFF.so
%{_libdir}/libvtkIOGeometry.so
%{_libdir}/libvtkIOHDF.so
%{_libdir}/libvtkIOImage.so
%{_libdir}/libvtkIOImport.so
%{_libdir}/libvtkIOInfovis.so
%{_libdir}/libvtkIOIOSS.so
%{_libdir}/libvtkIOLegacy.so
%{_libdir}/libvtkIOLSDyna.so
%{_libdir}/libvtkIOMINC.so
%{_libdir}/libvtkIOMotionFX.so
%{_libdir}/libvtkIOMovie.so
%{_libdir}/libvtkIONetCDF.so
%{_libdir}/libvtkIOOggTheora.so
%{_libdir}/libvtkIOParallelExodus.so
%{_libdir}/libvtkIOParallel.so
%{_libdir}/libvtkIOParallelXML.so
%{_libdir}/libvtkIOPLY.so
%{_libdir}/libvtkIOSegY.so
%{_libdir}/libvtkIOSQL.so
%{_libdir}/libvtkIOTecplotTable.so
%{_libdir}/libvtkIOVeraOut.so
%{_libdir}/libvtkIOVideo.so
%{_libdir}/libvtkIOXMLParser.so
%{_libdir}/libvtkIOXML.so
%{_libdir}/libvtkParallelCore.so
%{_libdir}/libvtkParallelDIY.so
%{_libdir}/libvtkRenderingAnnotation.so
%{_libdir}/libvtkRenderingCellGrid.so
%{_libdir}/libvtkRenderingContext2D.so
%{_libdir}/libvtkRenderingContextOpenGL2.so
%{_libdir}/libvtkRenderingCore.so
%{_libdir}/libvtkRenderingFreeType.so
%{?with_ffmpeg:%{_libdir}/libvtkRenderingFFMPEGOpenGL2.so}
%{_libdir}/libvtkRenderingGL2PSOpenGL2.so
%{_libdir}/libvtkRenderingHyperTreeGrid.so
%{_libdir}/libvtkRenderingImage.so
%{_libdir}/libvtkRenderingLabel.so
%{_libdir}/libvtkRenderingLICOpenGL2.so
%{_libdir}/libvtkRenderingLOD.so
%{_libdir}/libvtkRenderingOpenGL2.so
%{_libdir}/libvtkRenderingParallel.so
%{_libdir}/libvtkRenderingSceneGraph.so
%{_libdir}/libvtkRenderingUI.so
%{_libdir}/libvtkRenderingVolumeOpenGL2.so
%{_libdir}/libvtkRenderingVolume.so
%{_libdir}/libvtkRenderingVtkJS.so
%{_libdir}/libvtkTestingDataModel.so
%{_libdir}/libvtkTestingGenericBridge.so
%{_libdir}/libvtkTestingIOSQL.so
%{_libdir}/libvtkTestingRendering.so
%{_libdir}/libvtkViewsContext2D.so
%{_libdir}/libvtkViewsCore.so
%{_libdir}/libvtkViewsInfovis.so
%{_libdir}/libvtkWebCore.so
%{_libdir}/libvtkWebGLExporter.so
%{_libdir}/libvtkWrappingTools.so
%{_libdir}/libvtkCommonCache.so
%{_libdir}/libvtkFiltersMeshing.so
%{_libdir}/libvtkFiltersTemporal.so
%{_libdir}/libvtkIOAvmesh.so
%{_libdir}/libvtkIOERF.so
%{_libdir}/libvtkIOEngys.so
%{_libdir}/libvtkIOFDS.so
%{_libdir}/libvtkIOLANLX3D.so
%{_libdir}/libvtkRenderingGridAxes.so
%{_libdir}/libvtkRenderingVRModels.so
%{_libdir}/libvtkTestingCore.so
%{_libdir}/libvtkglad.so
%{_libdir}/libvtkscn.so
%{_libdir}/libvtktoken.so
%{_libdir}/libvtkx11.so
%{_libdir}/libvtkcgns.so
%{_libdir}/libvtkexodusII.so
%{_libdir}/libvtkfmt.so
%{_libdir}/libvtkgl2ps.so
%{_libdir}/libvtkioss.so
%{_libdir}/libvtkkissfft.so
%{_libdir}/libvtkloguru.so
%{_libdir}/libvtkmetaio.so
%{_libdir}/libvtksys.so
%{_libdir}/libvtkverdict.so
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
%{_includedir}/vtk/octree
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
%{_includedir}/vtk/GLTFSampler.h
%{_includedir}/vtk/token
%{_includedir}/vtk/vtkglad
%{_includedir}/vtk/vtkioss
%{_includedir}/vtk/vtkscn
%{_includedir}/vtk/vtkverdict
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/hierarchy

%if %{with java}
%exclude %{_includedir}/vtk/vtkJava*.h
%endif
%exclude %{_includedir}/vtk/vtkPython*.h
%{_libdir}/cmake/vtk

%files qt
%defattr(644,root,root,755)
%{_libdir}/libvtkGUISupportQt.so.*.*
%ghost %{_libdir}/libvtkGUISupportQt.so.1
%{_libdir}/libvtkGUISupportQtQuick.so.*.*
%ghost %{_libdir}/libvtkGUISupportQtQuick.so.1
%{_libdir}/libvtkGUISupportQtSQL.so.*.*
%ghost %{_libdir}/libvtkGUISupportQtSQL.so.1
%{_libdir}/libvtkRenderingQt.so.*.*
%ghost %{_libdir}/libvtkRenderingQt.so.1
%{_libdir}/libvtkViewsQt.so.*.*
%ghost %{_libdir}/libvtkViewsQt.so.1

%files qt-devel
%defattr(644,root,root,755)
%{_libdir}/libvtkGUISupportQt.so
%{_libdir}/libvtkGUISupportQtQuick.so
%{_libdir}/libvtkGUISupportQtSQL.so
%{_libdir}/libvtkRenderingQt.so
%{_libdir}/libvtkViewsQt.so
%{_includedir}/vtk/QFilterTreeProxyModel.h
%{_includedir}/vtk/QQuickVTKInteractorAdapter.h
%{_includedir}/vtk/QQuickVTKItem.h
%{_includedir}/vtk/QQuickVTKPinchEvent.h
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
%{_libdir}/libvtkJava.so.*.*
%ghost %{_libdir}/libvtkJava.so.1
# java modules
%dir %{_libdir}/java/vtk-*
%{_libdir}/java/vtk-*/libvtk*Java.so
%{_libdir}/java/vtk.jar

%files java-devel
%defattr(644,root,root,755)
%{_libdir}/libvtkJava.so
%exclude %{_includedir}/vtk/vtkJava*.h
%endif

%files python3
%defattr(644,root,root,755)
%doc Wrapping/Python/README*
%attr(755,root,root) %{_bindir}/vtkWrapPython
%attr(755,root,root) %{_bindir}/vtkWrapPythonInit
%attr(755,root,root) %{_bindir}/vtkpython
%{_libdir}/libvtkCommonPython.so.*.*
%ghost %{_libdir}/libvtkCommonPython.so.1
%{_libdir}/libvtkFiltersPython.so.*.*
%ghost %{_libdir}/libvtkFiltersPython.so.1
%{_libdir}/libvtkPythonContext2D.so.*.*
%ghost %{_libdir}/libvtkPythonContext2D.so.1
%{_libdir}/libvtkPythonInterpreter.so.*.*
%ghost %{_libdir}/libvtkPythonInterpreter.so.1
%{_libdir}/libvtkWrappingPythonCore3*.so.*.*
%ghost %{_libdir}/libvtkWrappingPythonCore3*.so.1
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
%{_libdir}/libvtkCommonPython.so
%{_libdir}/libvtkFiltersPython.so
%{_libdir}/libvtkPythonContext2D.so
%{_libdir}/libvtkPythonInterpreter.so
%{_libdir}/libvtkWrappingPythonCore3*.so
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
%dir %{_datadir}/vtk-%{vtk_base_version}
%{_datadir}/vtk-%{vtk_base_version}/Data
