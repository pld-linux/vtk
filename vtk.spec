# TODO:
# - handle VTK_USE_MPEG2_ENCODER (see CMakeLists.txt)
# - handle MPI and VTK_USE_PARALLEL_BGL (Parallel Boost Graph Library, BR: boost >= 1.40)
# - more system libraries? (check for VTK_THIRD_PARTY_SUBDIR in Utilities/CMakeLists.txt)
# - CUDA for Accelerators/Piston (on bcond)
# - NVCtrlLib for Rendering/OpenGL (on bcond)
# - VTK_USE_SYSTEM_XDMF2=ON ? (but our xdmf-devel seems not compatible)
# - python bcond?
#
# Conditional build
%bcond_without	java		# Java wrappers
%bcond_without	ffmpeg		# FFMPEG .avi saving support
%bcond_with	doc		# do not build and package doxygen documentation
%bcond_with	OSMesa		# build with OSMesa (https://bugzilla.redhat.com/show_bug.cgi?id=744434)
%bcond_with	system_gl2ps	# use system gl2ps (VTK currently is carrying local modifications to gl2ps)

Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl.UTF-8):	Zestaw narzędzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
Version:	8.2.0
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://www.vtk.org/files/release/8.2/VTK-%{version}.tar.gz
# Source0-md5:	8af3307da0fc2ef8cafe4a312b821111
Source1:	http://www.vtk.org/files/release/8.2/VTKData-%{version}.tar.gz
# Source1-md5:	a6eab7bc02cee1376ee69243dde373ce
Patch0:		vtk-abi.patch
Patch1:		gcc10.patch
Patch2:		proj6_compat.patch
Patch3:		qt-5.15.patch
Patch4:		python-3.8.patch
Patch5:		link.patch
URL:		http://www.vtk.org/
%{?with_OSMesa:BuildRequires: Mesa-libOSMesa-devel}
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Designer-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5XmlPatterns-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	R
BuildRequires:	boost-devel >= 1.39
BuildRequires:	cmake >= 2.8.8
%{?with_doc:BuildRequires:	doxygen}
BuildRequires:	expat-devel
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gdal-devel
%{?with_system_gl2ps:BuildRequires:	gl2ps-devel >= 1.3.8}
BuildRequires:	gnuplot
BuildRequires:	graphviz
BuildRequires:	hdf5-devel
%if %{with java}
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
%endif
BuildRequires:	jsoncpp-devel
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
BuildRequires:	netcdf-cxx-devel >= 4
# some code using it exists (Domains/Chemistry), but is not included in cmakefiles
#BuildRequires:	openqube-devel
BuildRequires:	perl-base
BuildRequires:	postgresql-devel
BuildRequires:	proj-devel >= 6.0
BuildRequires:	python3-devel
BuildRequires:	python3-sip-devel
BuildRequires:	qt5-build >= 4.5.0
BuildRequires:	qt5-qmake >= 4.5.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sip
BuildRequires:	sip-PyQt5
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
BuildRequires:	zlib-devel
BuildConflicts:	libXNVCtrl-devel
%{?with_system_gl2ps:Requires:	gl2ps >= 1.3.8}
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
Summary:	Qt5 bindings and Qt5 Designer plugin for VTK
Summary(pl.UTF-8):	Wiązania Qt5 oraz wtyczka Qt5 Designera do VTK
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core >= 4.5.0
Requires:	Qt5Gui >= 4.5.0
Requires:	Qt5Network >= 4.5.0
Requires:	Qt5OpenGL >= 4.5.0
Requires:	Qt5Sql >= 4.5.0
Requires:	Qt5WebKit >= 4.5.0

%description qt
Qt5 bindings and Qt5 Designer plugin for VTK.

%description qt -l pl.UTF-8
Wiązania Qt5 oraz wtyczka Qt5 Designera do VTK.

%package qt-devel
Summary:	Header files for VTK Qt5 bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań Qt5` do VTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	Qt5Core-devel >= 4.5.0
Requires:	Qt5Gui-devel >= 4.5.0
Requires:	Qt5OpenGL-devel >= 4.5.0
Requires:	Qt5Sql-devel >= 4.5.0

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
Obsoletes:	vtk-python-qt < 6.0.0-1
Obsoletes:	vtk-python-sip < 6.0.0-1
Obsoletes:	vtk-python < 8.2.0-1

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
%setup -q -n VTK-%{version} -b 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Replace relative path ../../../VTKData with destination filesystem path
grep -Erl '(\.\./)+VTKData' Examples | xargs \
  perl -pi -e 's,(\.\./)+VTKData,%{_datadir}/vtk-8.1,g'

# Save an unbuilt copy of the Example's sources for %doc
mkdir vtk-examples
cp -a Examples vtk-examples
# Don't ship Win32 examples
%{__rm} -r vtk-examples/Examples/GUI/Win32
find vtk-examples -type f | xargs chmod -R a-x

%build
export CFLAGS="%{rpmcflags} -D_UNICODE -DHAVE_UINTPTR_T"
export CXXFLAGS="%{rpmcxxflags} -D_UNICODE -DHAVE_UINTPTR_T"
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
	-DCMAKE_ASM_COMPILER="${cc#ccache }" \
	"
else
	ccache="
	-DCMAKE_C_COMPILER="%{__cc}" \
	-DCMAKE_CXX_COMPILER="%{__cxx}" \
	-DCMAKE_ASM_COMPILER="%{__cc}" \
	"
fi

mkdir -p build
cd build
%cmake .. \
	$ccache \
	-Wno-dev \
	%{cmake_on_off doc DBUILD_DOCUMENTATION} \
	-DBUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DOPENGL_INCLUDE_PATH:PATH=%{_includedir}/GL \
	-DPYTHON_INCLUDE_PATH:PATH=%{py3_incdir} \
	-DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{py3_ver}.so \
	-DPYTHON_UTIL_LIBRARY:PATH=%{_libdir}/libutil.so \
	-DTCL_INCLUDE_PATH:PATH=%{_includedir} \
	-DTCL_LIBRARY:PATH=%{_libdir}/libtcl.so \
	-DTK_INCLUDE_PATH:PATH=%{_includedir} \
	-DTK_LIBRARY:PATH=%{_libdir}/libtk.so \
	-DVTK_CUSTOM_LIBRARY_SUFFIX="" \
	-DVTK_INSTALL_ARCHIVE_DIR:PATH=%{_lib}/vtk \
	-DVTK_INSTALL_INCLUDE_DIR:PATH=include/vtk \
	-DVTK_INSTALL_LIBRARY_DIR:PATH=%{_lib}/vtk \
	-DVTK_INSTALL_PACKAGE_DIR:PATH=%{_lib}/cmake/vtk \
	-DVTK_INSTALL_TCL_DIR:PATH=share/tcl%{tcl_version}/vtk \
	-DVTK_INSTALL_QT_DIR=/%{_lib}/qt5/plugins/designer \
	-DVTK_FFMPEG_HAS_OLD_HEADER:BOOL=OFF \
	%{?with_OSMesa:-DVTK_OPENGL_HAS_OSMESA:BOOL=ON} \
	-DVTK_USE_SYSTEM_LIBRARIES:BOOL=ON \
	-DVTK_USE_OGGTHEORA_ENCODER:BOOL=ON \
	-DVTK_USE_SYSTEM_HDF5:BOOL=ON \
	-DVTK_USE_SYSTEM_XDMF2:BOOL=OFF \
	-DVTK_USE_SYSTEM_LIBHARU:BOOL=OFF \
	%{!?with_system_gl2ps:-DVTK_USE_SYSTEM_GL2PS:BOOL=OFF} \
%if %{with java}
	-DVTK_WRAP_JAVA:BOOL=ON \
	-DJAVA_INCLUDE_PATH:PATH=$JAVA_HOME/include \
	-DJAVA_INCLUDE_PATH2:PATH=$JAVA_HOME/include/linux \
	-DJAVA_AWT_INCLUDE_PATH:PATH=$JAVA_HOME/include \
%else
	-DVTK_WRAP_JAVA:BOOL=OFF \
%endif
	-DVTK_WRAP_PYTHON:BOOL=ON \
	-DVTK_PYTHON_VERSION=3 \
	%{?with_sip:-DVTK_WRAP_PYTHON_SIP:BOOL=ON} \
	-DVTK_Group_Imaging:BOOL=ON \
	-DVTK_Group_Qt:BOOL=ON \
	-DVTK_Group_Rendering:BOOL=ON \
	-DVTK_Group_StandAlone:BOOL=ON \
	-DVTK_Group_Tk:BOOL=ON \
	-DVTK_Group_Views:BOOL=ON \
	-DModule_vtkFiltersReebGraph:BOOL=ON \
	%{?with_ffmpeg:-DModule_vtkIOFFMPEG:BOOL=ON} \
	-DModule_vtkIOGDAL:BOOL=ON \
	-DModule_vtkIOGeoJSON:BOOL=ON \
	-DModule_vtkIOMySQL:BOOL=ON \
	-DModule_vtkIOODBC:BOOL=ON \
	-DModule_vtkIOParallelExodus:BOOL=ON \
	-DModule_vtkIOParallelLSDyna:BOOL=ON \
	-DModule_vtkIOPostgreSQL:BOOL=ON \
	-DModule_vtkIOVPIC:BOOL=ON \
	-DModule_vtkIOXdmf2:BOOL=ON \
	-DModule_vtkInfovisBoost:BOOL=ON \
	-DModule_vtkInfovisBoostGraphAlgorithms:BOOL=ON \
	-DModule_vtkRenderingFreeTypeFontConfig:BOOL=ON \
	-DModule_vtkRenderingMatplotlib:BOOL=ON \
	-DModule_vtkRenderingParallel:BOOL=ON
# TODO: -DModule_vtkAcceleratorsDax:BOOL=ON (BR: FindDax.cmake, maybe http://www.daxtoolkit.org/ ?)
# TODO:	-DModule_vtkAcceleratorsPiston:BOOL=ON (on bcond, BR: CUDA)
# TODO:	-DModule_vtkFiltersParallelFlowPaths:BOOL=ON (BR: MPI)
# TODO:	-DModule_vtkFiltersParallelStatistics:BOOL=ON (BR: MPI)
# TODO:	-DModule_vtkInfovisParallel:BOOL=ON (BR: MPI)
# TODO:	-DModule_vtkRenderingParallelLIC:BOOL=ON (BR: MPI)

%{__make}
%{?with_doc:%{__make} DoxygenDoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/ld.so.conf.d,%{_examplesdir}/%{name}-%{version}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# ld config
echo %{_libdir}/vtk > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/vtk-%{_arch}.conf

for f in $(cd build/ExternalData/Testing ; find Data -type l); do
	install -Dp build/ExternalData/Testing/$f $RPM_BUILD_ROOT%{_datadir}/vtk-8.1/$f
done

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
ImageSlicing \
LabeledMesh \
Medical1 \
Medical2 \
Medical3 \
Medical4 \
MultiBlock \
ParticleReader \
RGrid \
SGrid \
SimpleView \
Slider \
Slider2D \
SpecularSpheres \
TubesWithVaryingRadiusAndColors \
finance ; do
	install build/bin/$f $RPM_BUILD_ROOT%{_bindir}
done

# Install test binaries
for f in build/bin/*Tests build/bin/Test*; do
	install $f $RPM_BUILD_ROOT%{_bindir}
done

%if %{with java}
install -p build/bin/VTKJavaExecutable $RPM_BUILD_ROOT%{_bindir}
%endif
install -p build/bin/vtkpython $RPM_BUILD_ROOT%{_bindir}

# unwanted doxygen files and misplaced verdict docs
%{?with_doc:%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/vtk-*/{doxygen,verdict}}

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

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md vtkBanner.gif vtkLogo.ico Wrapping/Tools/README*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ld.so.conf.d/vtk-%{_arch}.conf
%dir %{_libdir}/vtk
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryOpenGL2.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistry.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFilters*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInteraction*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIO*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkLocalExample.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingAnnotation.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContext2D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContextOpenGL2.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeTypeFontConfig.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeType.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingGL2PSOpenGL2.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingImage.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLabel.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLOD.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingOpenGL2.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingParallel.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeOpenGL2.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolume.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkTesting*.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovis.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovis.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkVPIC.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkgl2ps.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtklibharu.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkxdmf2.so.1
%if %{with java}
%exclude %{_libdir}/vtk/libvtk*Java.so.1
%endif
%exclude %{_libdir}/vtk/libvtk*Python3?D.so.1
%exclude %{_libdir}/vtk/libvtkWrappingPython3?Core.so.1

%files devel
%defattr(644,root,root,755)
%doc Utilities/Upgrading/*
%attr(755,root,root) %{_bindir}/vtkWrapHierarchy
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryOpenGL2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistry.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFilters*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovis*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteraction*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIO*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkLocalExample.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingAnnotation.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContext2D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContextOpenGL2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeTypeFontConfig.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeType.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingGL2PSOpenGL2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingImage.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLabel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLOD.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingOpenGL2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingParallel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeOpenGL2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolume.so
%attr(755,root,root) %{_libdir}/vtk/libvtkTesting*.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkVPIC.so
%attr(755,root,root) %{_libdir}/vtk/libvtkgl2ps.so
%attr(755,root,root) %{_libdir}/vtk/libvtklibharu.so
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so
%attr(755,root,root) %{_libdir}/vtk/libvtkxdmf2.so
%if %{with java}
%exclude %{_libdir}/vtk/libvtk*Java.so
%endif
%exclude %{_libdir}/vtk/libvtk*Python3?D.so
%exclude %{_libdir}/vtk/libvtkWrappingPython3?Core.so
%{_libdir}/vtk/libvtkWrappingTools.a
%dir %{_includedir}/vtk
%{_includedir}/vtk/VPIC
%{_includedir}/vtk/DICOM*.h
%{_includedir}/vtk/DatabaseSchemaWith2Tables.h
%{_includedir}/vtk/vtkgl2ps
%{_includedir}/vtk/vtkkwiml
%{_includedir}/vtk/vtklibharu
%{_includedir}/vtk/vtkmetaio
%{_includedir}/vtk/vtksys
%{_includedir}/vtk/vtkverdict
%{_includedir}/vtk/vtkxdmf2
%{_includedir}/vtk/vtk*.h
%{_includedir}/vtk/vtk*.txx
%exclude %{_includedir}/vtk/vtkEventQtSlotConnect.h
%exclude %{_includedir}/vtk/vtkGUISupportQt*.h
%if %{with java}
%exclude %{_includedir}/vtk/vtkJavaUtil.h
%exclude %{_includedir}/vtk/vtkWrappingJavaModule.h
%endif
%exclude %{_includedir}/vtk/vtkPython*.h
%exclude %{_includedir}/vtk/vtkQImageToImageSource.h
%exclude %{_includedir}/vtk/vtkQt*.h
%exclude %{_includedir}/vtk/vtkRenderingQtModule.h
%exclude %{_includedir}/vtk/vtkTk*.h
%exclude %{_includedir}/vtk/vtkViewsQtModule.h
%{_libdir}/cmake/vtk

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQt.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQtSQL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingQt.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsQt.so.1
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libQVTKWidgetPlugin.so

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQt.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGUISupportQtSQL.so
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
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryOpenGL2Java.so
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

%files python3
%defattr(644,root,root,755)
%doc Wrapping/Python/README*
%attr(755,root,root) %{_bindir}/vtkWrapPython
%attr(755,root,root) %{_bindir}/vtkWrapPythonInit
%attr(755,root,root) %{_bindir}/vtkpython
%attr(755,root,root) %{_libdir}/vtk/libvtk*Python2?D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonInterpreter.so.1
# RenderingMatplotlib requires PythonInterpreter
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingMatplotlib.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingPythonTkWidgets-8.1.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWrappingPython2?Core.so.1
%dir %{py3_sitedir}/vtk
%{py3_sitedir}/vtk/*.py[co]
%dir %{py3_sitedir}/vtk/gtk
%{py3_sitedir}/vtk/gtk/*.py[co]
%dir %{py3_sitedir}/vtk/numpy_interface
%{py3_sitedir}/vtk/numpy_interface/*.py[co]
%dir %{py3_sitedir}/vtk/qt
%{py3_sitedir}/vtk/qt/*.py[co]
%dir %{py3_sitedir}/vtk/qt4
%{py3_sitedir}/vtk/qt4/*.py[co]
%dir %{py3_sitedir}/vtk/test
%{py3_sitedir}/vtk/test/*.py[co]
%dir %{py3_sitedir}/vtk/tk
%{py3_sitedir}/vtk/tk/*.py[co]
%dir %{py3_sitedir}/vtk/util
%{py3_sitedir}/vtk/util/*.py[co]
%dir %{py3_sitedir}/vtk/wx
%{py3_sitedir}/vtk/wx/*.py[co]
%attr(755,root,root) %{py_sitedir}/vtk/vtk*Python.so

%files python3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtk*Python3?D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonInterpreter.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingMatplotlib.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWrappingPython3?Core.so
%{_includedir}/vtk/PyVTK*.h
%{_includedir}/vtk/vtkPython*.h

%files tcl
%defattr(644,root,root,755)
%doc Wrapping/Tcl/README*
%attr(755,root,root) %{_bindir}/vtkWrapTcl
%attr(755,root,root) %{_bindir}/vtkWrapTclInit
%attr(755,root,root) %{_bindir}/vtk
%{_datadir}/tcl%{tcl_version}/vtk

%files tcl-devel
%defattr(644,root,root,755)
%{_includedir}/vtk/vtkTcl*.h
%{_includedir}/vtk/vtkTk*.h

%files test-suite
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*Tests
%attr(755,root,root) %{_bindir}/Test*

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
%attr(755,root,root) %{_bindir}/Medical4
%attr(755,root,root) %{_bindir}/MultiBlock
%attr(755,root,root) %{_bindir}/RGrid
%attr(755,root,root) %{_bindir}/SGrid
%attr(755,root,root) %{_bindir}/SimpleView
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
%attr(755,root,root) %{_bindir}/ImageSlicing
%attr(755,root,root) %{_bindir}/LabeledMesh
%attr(755,root,root) %{_bindir}/ParticleReader
%attr(755,root,root) %{_bindir}/Slider
%attr(755,root,root) %{_bindir}/Slider2D
%attr(755,root,root) %{_bindir}/TubesWithVaryingRadiusAndColors
%{_examplesdir}/%{name}-%{version}

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/vtk-8.1
%{_datadir}/vtk-8.1/Data
