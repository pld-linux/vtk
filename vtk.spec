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

Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl.UTF-8):	Zestaw narzędzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
Version:	8.2.0
Release:	14
License:	BSD
Group:		Libraries
#Source0Download: https://vtk.org/download/
Source0:	https://www.vtk.org/files/release/8.2/VTK-%{version}.tar.gz
# Source0-md5:	8af3307da0fc2ef8cafe4a312b821111
Source1:	https://www.vtk.org/files/release/8.2/VTKData-%{version}.tar.gz
# Source1-md5:	a6eab7bc02cee1376ee69243dde373ce
Patch0:		%{name}-pugixml.patch
Patch1:		gcc10.patch
Patch2:		proj6_compat.patch
Patch3:		qt-5.15.patch
Patch4:		python-3.8.patch
Patch5:		link.patch
Patch6:		system-pugixml.patch
Patch7:		freetype.patch
Patch8:		%{name}-doc.patch
URL:		https://vtk.org/
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
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
%endif
BuildRequires:	jsoncpp-devel >= 0.7.0
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
BuildRequires:	pugixml-devel
BuildRequires:	python3-devel
BuildRequires:	qt5-build >= 4.5.0
BuildRequires:	qt5-qmake >= 4.5.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
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

%define		skip_post_check_so	lib.*Python.*\.so.*

%description
The Visualization ToolKit (VTK) is an object oriented software system
for 3D computer graphics, image processing, and visualization. VTK
includes a textbook, a C++ class library, and several interpreted
interface layers including Java, and Python. VTK supports a
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
kilka interpretowanych warstw interfejsów, w tym dla Javy i
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
Requires:	double-conversion-devel
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

%package examples
Summary:	C++ and Python example programs/scripts for VTK
Summary(pl.UTF-8):	Przykładowe programy/skrypty w C++ i Pythonie dla VTK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}

%description examples
This package contains all the examples from the VTK source. To compile
the C++ examples you will need to install the vtk-devel package as
well. The Python examples can be run with the corresponding
packages (vtk-python3).

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# Replace relative path ../../../VTKData with destination filesystem path
grep -Erl '(\.\./)+VTKData' Examples | xargs \
	%{__perl} -pi -e 's,(\.\./)+VTKData,%{_datadir}/vtk-8.2,g'

# Save an unbuilt copy of the Example's sources for %doc
mkdir vtk-examples
cp -a Examples vtk-examples
# Don't ship Win32 examples
%{__rm} -r vtk-examples/Examples/GUI/Win32
find vtk-examples -type f | xargs chmod -R a-x

for x in doubleconversion eigen expat freetype %{?with_system_gl2ps:gl2ps }glew hdf5 jpeg jsoncpp libproj libxml2 lz4 lzma netcdf ogg png pugixml sqlite theora tiff zfp zlib; do
%{__rm} -r ThirdParty/*/vtk$x
done

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
	%{cmake_on_off doc BUILD_DOCUMENTATION} \
	-DBUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DDOXYGEN_GENERATE_HTMLHELP=OFF \
	-DOPENGL_INCLUDE_PATH:PATH=%{_includedir}/GL \
	-DPYTHON_INCLUDE_PATH:PATH=%{py3_incdir} \
	-DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{py3_ver}.so \
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
	-DVTK_INSTALL_PYTHON_MODULES_DIR:PATH=%{py3_sitedir} \
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

%if %{with doc}
%{__make} DoxygenDoc
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/ld.so.conf.d,%{_examplesdir}/%{name}-%{version}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# disable completeness check incompatible with split packaging
%{__sed} -i -e '/^foreach(target .*IMPORT_CHECK_TARGETS/,/^endforeach/d; /^unset(_IMPORT_CHECK_TARGETS)/d' $RPM_BUILD_ROOT%{_libdir}/cmake/vtk/VTKTargets.cmake

# ld config
echo %{_libdir}/vtk > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/vtk-%{_arch}.conf

for f in $(cd build/ExternalData/Testing ; find Data -type l); do
	install -Dp build/ExternalData/Testing/$f $RPM_BUILD_ROOT%{_datadir}/vtk-8.2/$f
done

# proprietary font, even not used; invalid UTF-8 in signature returned by libmagic)
# (commented out in Views/Infovis/Testing/Cxx/TestQtLabelStrategy.cxx)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vtk-8.2/Data/Infovis/DaveDS_-_Sketchy.ttf

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

%files
%defattr(644,root,root,755)
%doc README.md vtkBanner.gif vtkLogo.ico Wrapping/Tools/README*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ld.so.conf.d/vtk-%{_arch}.conf
%dir %{_libdir}/vtk
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonColor.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonComputationalGeometry.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonDataModel.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonExecutionModel.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMath.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMisc.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonSystem.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonTransforms.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryOpenGL2.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistry.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersAMR.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersExtraction.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersFlowPaths.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeneral.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeneric.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeometry.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHybrid.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHyperTree.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersImaging.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersModeling.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallel.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallelImaging.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPoints.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersProgrammable.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersReebGraph.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSMP.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSelection.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSources.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersStatistics.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTexture.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTopology.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersVerdict.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAMR.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAsynchronous.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCityGML.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOEnSight.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExodus.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExport.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportOpenGL2.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportPDF.so.1
%{?with_ffmpeg:%attr(755,root,root) %{_libdir}/vtk/libvtkIOFFMPEG.so.1}
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGDAL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeoJSON.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeometry.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImage.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImport.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOInfovis.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLSDyna.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLegacy.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMINC.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMovie.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMySQL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIONetCDF.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOODBC.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPLY.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallel.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelExodus.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelLSDyna.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelXML.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPostgreSQL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSQL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSegY.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOTecplotTable.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVPIC.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVeraOut.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVideo.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXML.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXMLParser.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXdmf2.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingColor.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingFourier.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingGeneral.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingHybrid.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMath.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMorphological.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingSources.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStatistics.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStencil.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisBoostGraphAlgorithms.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisLayout.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionImage.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionStyle.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionWidgets.so.1
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
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingGenericBridge.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingIOSQL.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingRendering.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCore.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovis.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovis.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkVPIC.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkexodusII.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkgl2ps.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtklibharu.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkxdmf2.so.1

%files devel
%defattr(644,root,root,755)
%doc Utilities/Upgrading/*
%attr(755,root,root) %{_bindir}/vtkWrapHierarchy
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonColor.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonComputationalGeometry.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonDataModel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonExecutionModel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMath.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMisc.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonSystem.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonTransforms.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDICOMParser.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryOpenGL2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistry.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersAMR.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersExtraction.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersFlowPaths.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeneral.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeneric.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeometry.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHybrid.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHyperTree.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersImaging.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersModeling.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallelImaging.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPoints.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersProgrammable.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersReebGraph.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSMP.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSelection.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSources.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersStatistics.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTexture.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTopology.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersVerdict.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAMR.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAsynchronous.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCityGML.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOEnSight.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExodus.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExport.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportOpenGL2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportPDF.so
%{?with_ffmpeg:%attr(755,root,root) %{_libdir}/vtk/libvtkIOFFMPEG.so}
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGDAL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeoJSON.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeometry.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImage.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImport.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOInfovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLSDyna.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLegacy.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMINC.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMovie.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMySQL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIONetCDF.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOODBC.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPLY.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelExodus.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelLSDyna.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelXML.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPostgreSQL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSQL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSegY.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOTecplotTable.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVPIC.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVeraOut.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVideo.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXML.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXMLParser.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXdmf2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingColor.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingFourier.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingGeneral.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingHybrid.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMath.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMorphological.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingSources.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStatistics.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStencil.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisBoostGraphAlgorithms.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisLayout.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionImage.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionStyle.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionWidgets.so
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
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingGenericBridge.so
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingIOSQL.so
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingRendering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCore.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovis.so
%attr(755,root,root) %{_libdir}/vtk/libvtkVPIC.so
%attr(755,root,root) %{_libdir}/vtk/libvtkexodusII.so
%attr(755,root,root) %{_libdir}/vtk/libvtkgl2ps.so
%attr(755,root,root) %{_libdir}/vtk/libvtklibharu.so
%attr(755,root,root) %{_libdir}/vtk/libvtkmetaio.so
%attr(755,root,root) %{_libdir}/vtk/libvtksys.so
%attr(755,root,root) %{_libdir}/vtk/libvtkverdict.so
%attr(755,root,root) %{_libdir}/vtk/libvtkxdmf2.so
%{_libdir}/vtk/libvtkWrappingTools.a
%dir %{_includedir}/vtk
%{_includedir}/vtk/VPIC
%{_includedir}/vtk/DICOM*.h
%{_includedir}/vtk/DatabaseSchemaWith2Tables.h
%{_includedir}/vtk/LSDyna*.h
%{_includedir}/vtk/vtkexodusII
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
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonColorJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonComputationalGeometryJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonDataModelJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonExecutionModelJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMathJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMiscJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonSystemJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonTransformsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryOpenGL2Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersAMRJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersExtractionJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersFlowPathsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeneralJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGenericJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeometryJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHybridJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHyperTreeJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersImagingJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersModelingJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallelJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallelImagingJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPointsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersProgrammableJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersReebGraphJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSMPJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSelectionJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSourcesJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersStatisticsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTextureJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTopologyJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersVerdictJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAMRJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAsynchronousJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCityGMLJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOEnSightJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExodusJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportOpenGL2Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportPDFJava.so
%{?with_ffmpeg:%attr(755,root,root) %{_libdir}/vtk/libvtkIOFFMPEGJava.so}
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGDALJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeoJSONJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeometryJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImageJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImportJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOInfovisJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLSDynaJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLegacyJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMINCJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMovieJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMySQLJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIONetCDFJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOODBCJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPLYJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelExodusJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelLSDynaJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelXMLJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPostgreSQLJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSQLJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSegYJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOTecplotTableJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVPICJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVeraOutJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVideoJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXMLJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXMLParserJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXdmf2Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingColorJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingFourierJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingGeneralJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingHybridJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMathJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMorphologicalJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingSourcesJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStatisticsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStencilJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisBoostGraphAlgorithmsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisLayoutJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionImageJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionStyleJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionWidgetsJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkLocalExampleJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingAnnotationJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContext2DJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContextOpenGL2Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeTypeJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingGL2PSOpenGL2Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingImageJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLODJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLabelJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingMatplotlibJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingOpenGL2Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingParallelJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingQtJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeOpenGL2Java.so
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingRenderingJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2DJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCoreJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovisJava.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovisJava.so
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
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonColorPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonComputationalGeometryPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonDataModelPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonExecutionModelPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMathPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMiscPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonSystemPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonTransformsPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryOpenGL2Python3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersAMRPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersExtractionPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersFlowPathsPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeneralPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGenericPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeometryPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHybridPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHyperTreePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersImagingPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersModelingPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallelPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallelImagingPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPointsPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersProgrammablePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPython.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPythonPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersReebGraphPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSMPPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSelectionPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSourcesPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersStatisticsPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTexturePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTopologyPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersVerdictPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAMRPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAsynchronousPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCityGMLPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOEnSightPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExodusPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportOpenGL2Python3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportPDFPython3*D.so.1
%{?with_ffmpeg:%attr(755,root,root) %{_libdir}/vtk/libvtkIOFFMPEGPython3*D.so.1}
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGDALPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeoJSONPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeometryPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImagePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImportPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOInfovisPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLSDynaPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLegacyPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMINCPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMoviePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMySQLPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIONetCDFPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOODBCPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPLYPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelExodusPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelLSDynaPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelXMLPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPostgreSQLPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSQLPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSegYPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOTecplotTablePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVPICPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVeraOutPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVideoPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXMLPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXMLParserPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXdmf2Python3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingColorPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingFourierPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingGeneralPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingHybridPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMathPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMorphologicalPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingSourcesPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStatisticsPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStencilPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisBoostGraphAlgorithmsPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisLayoutPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionImagePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionStylePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionWidgetsPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonContext2D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonContext2DPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonInterpreter.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingAnnotationPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContext2DPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContextOpenGL2Python3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeTypePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingGL2PSOpenGL2Python3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingImagePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLODPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLabelPython3*D.so.1
# RenderingMatplotlib requires PythonInterpreter
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingMatplotlib.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingMatplotlibPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingOpenGL2Python3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingParallelPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingQtPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeOpenGL2Python3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingRenderingPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2DPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCorePython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovisPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovisPython3*D.so.1
%attr(755,root,root) %{_libdir}/vtk/libvtkWrappingPython3*Core.so.1
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
%dir %{py3_sitedir}/vtkmodules/qt4
%{py3_sitedir}/vtkmodules/qt4/*.py
%{py3_sitedir}/vtkmodules/qt4/__pycache__
%dir %{py3_sitedir}/vtkmodules/test
%{py3_sitedir}/vtkmodules/test/*.py
%{py3_sitedir}/vtkmodules/test/__pycache__
%dir %{py3_sitedir}/vtkmodules/tk
%{py3_sitedir}/vtkmodules/tk/__pycache__
%{py3_sitedir}/vtkmodules/tk/*.py
%dir %{py3_sitedir}/vtkmodules/util
%{py3_sitedir}/vtkmodules/util/*.py
%{py3_sitedir}/vtkmodules/util/__pycache__
%dir %{py3_sitedir}/vtkmodules/wx
%{py3_sitedir}/vtkmodules/wx/*.py
%{py3_sitedir}/vtkmodules/wx/__pycache__
%attr(755,root,root) %{py3_sitedir}/vtkmodules/vtk*Python.so

%files python3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vtk/libvtkChartsCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonColorPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonComputationalGeometryPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonDataModelPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonExecutionModelPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMathPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonMiscPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonSystemPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkCommonTransformsPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkDomainsChemistryOpenGL2Python3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersAMRPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersExtractionPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersFlowPathsPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeneralPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGenericPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersGeometryPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHybridPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersHyperTreePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersImagingPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersModelingPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallelPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersParallelImagingPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPointsPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersProgrammablePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPython.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersPythonPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersReebGraphPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSMPPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSelectionPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersSourcesPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersStatisticsPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTexturePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersTopologyPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltersVerdictPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGeovisCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAMRPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOAsynchronousPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCityGMLPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOEnSightPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExodusPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportOpenGL2Python3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOExportPDFPython3*D.so
%{?with_ffmpeg:%attr(755,root,root) %{_libdir}/vtk/libvtkIOFFMPEGPython3*D.so}
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGDALPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeoJSONPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOGeometryPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImagePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOImportPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOInfovisPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLSDynaPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOLegacyPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMINCPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMoviePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOMySQLPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIONetCDFPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOODBCPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPLYPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelExodusPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelLSDynaPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOParallelXMLPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOPostgreSQLPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSQLPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOSegYPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOTecplotTablePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVPICPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVeraOutPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOVideoPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXMLPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXMLParserPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIOXdmf2Python3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingColorPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingFourierPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingGeneralPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingHybridPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMathPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingMorphologicalPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingSourcesPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStatisticsPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImagingStencilPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisBoostGraphAlgorithmsPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInfovisLayoutPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionImagePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionStylePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkInteractionWidgetsPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallelCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonContext2D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonContext2DPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkPythonInterpreter.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingAnnotationPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContext2DPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingContextOpenGL2Python3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingFreeTypePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingGL2PSOpenGL2Python3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingImagePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLODPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingLabelPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingMatplotlib.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingMatplotlibPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingOpenGL2Python3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingParallelPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingPythonTkWidgets-8.2.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingQtPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRenderingVolumeOpenGL2Python3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkTestingRenderingPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsContext2DPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsCorePython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsGeovisPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkViewsInfovisPython3*D.so
%attr(755,root,root) %{_libdir}/vtk/libvtkWrappingPython3*Core.so
%{_includedir}/vtk/PyVTK*.h
%{_includedir}/vtk/vtkPython*.h

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
%dir %{_datadir}/vtk-8.2
%{_datadir}/vtk-8.2/Data
