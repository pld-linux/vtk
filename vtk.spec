#
# ToDo:
# - make it all work
#
# Conditional build
%bcond_with	java	# build with Java support (not yet done)
#
Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl.UTF-8):	Zestaw narzędzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
Version:	4.2.2
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/vtk/VTK-4.2-LatestRelease.tar.gz
# Source0-md5:	41382fb3f8d15e76d7464c11045ee7a5
Source1:	http://dl.sourceforge.net/vtk/VTKData-4.2.tar.gz
# Source1-md5:	2bbd1a62884906eac4f279441cbb9cfa
Patch0:		%{name}-cmakefiles.patch
URL:		http://public.kitware.com/VTK/
BuildRequires:	XFree86-devel
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	python-devel
BuildRequires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Summary(pl.UTF-8):	Dowiązania Tcl do VTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tcl
This package contains Tcl bindings for VTK.

%description tcl -l pl.UTF-8
Ten pakiet zawiera dowiązania Tcl dla VTK.

%package python
Summary:	Python bindings for VTK
Summary(pl.UTF-8):	Dowiązania Pythona do VTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
This package contains Python bindings for VTK.

%description python -l pl.UTF-8
Ten pakiet zawiera dowiązania Pythona dla VTK.

%package java
Summary:	Java bindings for VTK
Summary(pl.UTF-8):	Dowiązania Javy do VTK
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description java
This package contains Java bindings for VTK.

%description java -l pl.UTF-8
Ten pakiet zawiera dowiązania Javy dla VTK.

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

%description data
This package contains all the data from the VTKData repository. These
data are required to run various examples from the vtk-examples
package.

%description data -l pl.UTF-8
Ten pakiet zawiera wszystkie dane z repozytorium VTKData. Dane te są
potrzebne do uruchamiania różnych przykładów z pakietu vtk-examples.

%prep
%setup -q -n VTK-%{version} -a 1
cd Hybrid
%patch0 -p1

%build
#%if %build_java
#cmake 	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
#	-DLIBRARY_OUTPUT_PATH:PATH=$RPM_BUILD_DIR/VTK-%version/lib \
#	-DEXECUTABLE_OUTPUT_PATH:PATH=$RPM_BUILD_DIR/VTK-%version/bin \
#	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
#	-DCMAKE_SKIP_RPATH:BOOL=ON \
#	-DCMAKE_CXX_FLAGS:STRING="$RPM_OPT_FLAGS" \
#	-DCMAKE_C_FLAGS:STRING="$RPM_OPT_FLAGS"	\
#	-DJAVA_INCLUDE_PATH:PATH=$JAVA_HOME/include
#	-DJAVA_INCLUDE_PATH2:PATH=$JAVA_HOME/include/linux \
#	-DJAVE_AWT_INCLUDE_PATH:PATH=$JAVA_HOME/include \
#	-DPYTHON_INCLUDE_PATH:PATH=$(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'include', 'python' + sys.version[:3])") \
#	-DPYTHON_LIBRARY:FILEPATH=$(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'lib', 'python' + sys.version[:3], 'config/libpython' + sys.version[:3] + '.a')") \
#	-DVTK_DATA_ROOT:PATH=%{_docdir}/vtk-data-%{version} \
#	-DVTK_WRAP_PYTHON:BOOL=ON \
#	-DVTK_WRAP_JAVA:BOOL=ON \
#	-DVTK_WRAP_TCL:BOOL=ON \
#	-DVTK_USE_HYBRID:BOOL=ON \
#	-DVTK_USE_PARALLEL:BOOL=ON \
#	-DVTK_USE_RENDERING:BOOL=ON \
#	-DVTK_USE_X:BOOL=ON \
#	-DBUILD_DOCUMENTATION:BOOL=ON \
#	-DBUILD_EXAMPLES:BOOL=ON \
#	-DBUILD_SHARED_LIBS:BOOL=ON \
#	-DBUILD_TESTING:BOOL=ON \
#	-DOPENGL_INCLUDE_PATH:FILEPATH=/usr/X11R6/include/GL
##	-DOPENGL_LIBRARY:FILEPATH=/usr/X11R6/lib/libGL.so.1.0
#
#%else
#cmake	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
#	-DLIBRARY_OUTPUT_PATH:PATH=$RPM_BUILD_DIR/VTK-%version/lib \
#	-DEXECUTABLE_OUTPUT_PATH:PATH=$RPM_BUILD_DIR/VTK-%version/bin \
#	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
#	-DCMAKE_SKIP_RPATH:BOOL=ON \
#	-DCMAKE_CXX_FLAGS:STRING="$RPM_OPT_FLAGS" \
#	-DCMAKE_C_FLAGS:STRING="$RPM_OPT_FLAGS"	\
#	-DPYTHON_INCLUDE_PATH:PATH=$(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'include', 'python' + sys.version[:3])") \
#	-DPYTHON_LIBRARY:FILEPATH=$(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'lib', 'python' + sys.version[:3], 'config/libpython' + sys.version[:3] + '.a')") \
#	-DVTK_DATA_ROOT:PATH=%{_datadir}/vtk-data-%{version} \
#	-DVTK_WRAP_PYTHON:BOOL=ON \
#	-DVTK_WRAP_JAVA:BOOL=off \
#	-DVTK_WRAP_TCL:BOOL=ON \
#	-DVTK_USE_HYBRID:BOOL=ON \
#	-DVTK_USE_PARALLEL:BOOL=ON \
#	-DVTK_USE_RENDERING:BOOL=ON \
#	-DVTK_USE_X:BOOL=ON \
#	-DBUILD_DOCUMENTATION:BOOL=ON \
#	-DBUILD_EXAMPLES:BOOL=ON \
#	-DBUILD_SHARED_LIBS:BOOL=ON \
#	-DBUILD_TESTING:BOOL=ON \
# 	-DOPENGL_INCLUDE_PATH:FILEPATH=/usr/X11R6/include/GL
## 	-DOPENGL_LIBRARY:FILEPATH=/usr/X11R6/lib/libGL.so.1.0
#
#%endif
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DLIBRARY_OUTPUT_PATH:PATH=$RPM_BUILD_DIR/VTK-%{version}/lib \
	-DEXECUTABLE_OUTPUT_PATH:PATH=$RPM_BUILD_DIR/VTK-%{version}/bin \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
 	-DBUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_DOCUMENTATION:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-DCMAKE_BACKWARDS_COMPATIBILITY=1.8 \
	-DOPENGL_INCLUDE_PATH:PATH=%{_prefix}/X11R6/include/GL \
	-DPYTHON_INCLUDE_PATH:PATH=%{_includedir}/python2.3 \
	-DPYTHON_LIBRARY:FILEPATH=$(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'lib', 'python' + sys.version
	[:3], 'config/libpython' + sys.version[:3] + '.a')") \
	-DPYTHON_UTIL_LIBRARY:PATH=%{_libdir}/libutil.so \
	-DTCL_INCLUDE_PATH:PATH=%{_includedir} \
	-DTCL_LIBRARY:PATH=%{_libdir}/libtcl.so \
	-DTK_INCLUDE_PATH:PATH=%{_includedir} \
	-DTK_LIBRARY:PATH=%{_libdir}/libtk.so \
	-DVTK_DATA_ROOT:PATH=%{_datadir}/vtk \
	-DVTK_USE_HYBRID:BOOL=ON \
	-DVTK_USE_PARALLEL:BOOL=ON \
	-DVTK_USE_PATENTED:BOOL=off \
	-DVTK_USE_RENDERING:BOOL=ON \
	-DVTK_WRAP_JAVA:BOOL=OFF \
	-DVTK_WRAP_PYTHON:BOOL=ON \
	-DVTK_WRAP_TCL:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_CXX_COMPILER:PATH="%{__cxx}" \
	-DCMAKE_C_COMPILER:PATH="%{__cc}" \
	-DCMAKE_LINKER_FLAGS:STRING="%{rpmldflags}" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

#setup python
export VTKPYTHONPATH=%(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'lib', 'python' + sys.version[:3],'site-packages')")

#install directories
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk
install -d $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/gtk
install -d $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/qt
install -d $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/testing
install -d $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/tk
install -d $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/util
install -d $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/wx
install -d $RPM_BUILD_ROOT/$VTKPYTHONPATH
install -d $RPM_BUILD_ROOT%{_includedir}/vtk

#install libs and tcl
#%%makeinstall_std
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT%{_libdir}/vtk/*.so
for f in $RPM_BUILD_ROOT%{_libdir}/vtk/libvtk*Python*.so
do
	ln -s ../`basename $f` $RPM_BUILD_ROOT%{_libdir}/vtk/python/
done

#install binaries
install bin/* $RPM_BUILD_ROOT%{_bindir}

#install python
install Wrapping/Python/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python
install Wrapping/Python/vtk/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk
install Wrapping/Python/vtk/gtk/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/gtk
install Wrapping/Python/vtk/qt/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/qt
install Wrapping/Python/vtk/tk/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/tk
install Wrapping/Python/vtk/util/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/util
install Wrapping/Python/vtk/wx/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/wx
cat > $RPM_BUILD_ROOT/$VTKPYTHONPATH/vtkpython.pth <<_EOF
%{_libdir}/vtk/python
_EOF

%if %build_java
#install java
install -d $RPM_BUILD_ROOT%{_libdir}/vtk/java
install lib/vtk.jar $RPM_BUILD_ROOT%{_libdir}/vtk/java
install java/vtk/*.java $RPM_BUILD_ROOT%{_libdir}/vtk/java
%endif

#install data
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}-data
cp -r VTKData-release-4-2/* $RPM_BUILD_ROOT%{_datadir}/%{name}-data
rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}-data/CVS

#install test-suite and examples
for d in Common Filtering Graphics Hybrid IO Imaging Parallel Patented Rendering
do
	install -d $RPM_BUILD_ROOT%{_datadir}/vtk-examples/Testing/$d
	cp -a $d/Testing/* $RPM_BUILD_ROOT%{_datadir}/vtk-examples/Testing/$d
done
cp -a Examples $RPM_BUILD_ROOT%{_datadir}/vtk-examples

# get rid of unwanted files
find $RPM_BUILD_ROOT%{_datadir}/vtk-examples -name "*.o" -exec rm {} \;
find $RPM_BUILD_ROOT%{_datadir}/vtk-examples -name CMakeCache.txt -exec rm {} \;
find $RPM_BUILD_ROOT%{_datadir}/vtk-examples -name Makefile -exec rm {} \;
find $RPM_BUILD_ROOT%{_datadir}/vtk-examples -name DartTestfile.txt -exec rm {} \;
find $RPM_BUILD_ROOT%{_datadir}/vtk-examples -name .NoDartCoverage -exec rm {} \;
find $RPM_BUILD_ROOT%{_datadir}/vtk-examples -name "CMake*" -exec rm {} \;
find $RPM_BUILD_ROOT%{_datadir}/vtk-examples -name "cmake.*" -exec rm {} \;

# Generate the package testing-progs lists and store them in file-lists
echo "%defattr (644,root,root,755)" > testing-progs-list
%if %build_java
find ${RPM_BUILD_ROOT}/usr/bin -type f | \
	sed -e "s#^${RPM_BUILD_ROOT}##g" | \
	egrep -v '^/usr/bin/(vtk|pvtk|vtkWrap.*|vtkParse.*|VTKJavaExecutable|vtkpython|pvtkpython)$' \
	>> testing-progs-list
%else
find ${RPM_BUILD_ROOT}/usr/bin -type f | \
	sed -e "s#^${RPM_BUILD_ROOT}##g" | \
	egrep -v '^/usr/bin/(vtk|pvtk|vtkWrap.*|vtkParse.*|vtkpython|pvtkpython)$' \
	>> testing-progs-list
%endif

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

%files
%defattr(644,root,root,755)
%doc README.html vtkLogo.jpg
%dir %{_libdir}/vtk
%attr(755,root,root) %{_libdir}/vtk/libvtkCommon.so
%attr(755,root,root) %{_libdir}/vtk/libvtkFiltering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkGraphics.so
%attr(755,root,root) %{_libdir}/vtk/libvtkHybrid.so
%attr(755,root,root) %{_libdir}/vtk/libvtkImaging.so
%attr(755,root,root) %{_libdir}/vtk/libvtkIO.so
%attr(755,root,root) %{_libdir}/vtk/libvtkParallel.so
%attr(755,root,root) %{_libdir}/vtk/libvtkRendering.so
%attr(755,root,root) %{_libdir}/vtk/libvtkjpeg.so
%attr(755,root,root) %{_libdir}/vtk/libvtkpng.so
%attr(755,root,root) %{_libdir}/vtk/libvtkzlib.so
%attr(755,root,root) %{_libdir}/vtk/libvtkexpat.so
%attr(755,root,root) %{_libdir}/vtk/libvtkfreetype.so
%attr(755,root,root) %{_libdir}/vtk/libvtkftgl.so
%attr(755,root,root) %{_libdir}/vtk/libvtktiff.so

%files devel
%defattr(644,root,root,755)
%doc %{_libdir}/vtk/doxygen
%doc Utilities/Upgrading/*
%{_includedir}/vtk
%{_libdir}/vtk/CMake
%{_libdir}/vtk/*.cmake

%files test-suite -f testing-progs-list
%defattr(644,root,root,755)

%files tcl
%defattr(644,root,root,755)
%doc README.html vtkLogo.jpg
%dir %{_libdir}/vtk/testing
%attr(755,root,root) %{_bindir}/vtkWrapTcl
%attr(755,root,root) %{_bindir}/vtk
%attr(755,root,root) %{_libdir}/vtk/libvtk*TCL.so
%{_libdir}/vtk/tcl
%{_libdir}/vtk/testing/*.tcl

%files python
%defattr(644,root,root,755)
%dir %_libdir/vtk/testing
%attr(755,root,root) %{_bindir}/vtkWrapPython
%attr(755,root,root) %{_bindir}/vtkpython
%attr(755,root,root) %{_libdir}/vtk/libvtk*Python*.so
%{_libdir}/vtk/python
%{_libdir}/vtk/testing/*.py
%(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'lib', 'python' + sys.version[:3],'site-packages', 'vtkpython.pth')")

%if %build_java
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vtkParseJava
%attr(755,root,root) %{_bindir}/vtkWrapJava
%attr(755,root,root) %{_bindir}/VTKJavaExecutable
%attr(755,root,root) %{_libdir}/vtk/libvtk*Java.so
%{_libdir}/vtk/java
%endif

%files examples
%defattr(644,root,root,755)
%dir %{_datadir}/vtk-examples
%{_datadir}/vtk-examples/Examples
%{_datadir}/vtk-examples/Testing

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/vtk-data
%{_datadir}/vtk-data/Baseline
%{_datadir}/vtk-data/Data
%{_datadir}/vtk-data/VTKData.readme
