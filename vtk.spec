#
# ToDo:
# - make it all work 
# Conditional build
#
%bcond_with	java	# build with Java support (not yet done)
#

Summary:	Toolkit for 3D computer graphics, image processing, and visualization
Summary(pl):	Zestaw narzêdzi do trójwymiarowej grafiki, przetwarzania obrazu i wizualizacji
Name:		vtk
Version:	4.2.2
Release:	0.1
License:	BSD
Group:		Graphics
Source0:	%{name}42Src.tar.bz2
Source1:	%{name}42Data.tar.bz2
Patch0:		%{name}-cmakefiles.patch
URL:		http://public.kitware.com/VTK/
BuildRequires: 	cmake 
BuildRequires:	python-devel 
BuildRequires:	tcl 
BuildRequires:	XFree86-devel 
BuildRequires:	doxygen
BuildRoot: 	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Visualization ToolKit (VTK) is an object oriented software system
for 3D computer graphics, image processing, and visualization. VTK
includes a textbook, a C++ class library, and several interpreted
interface layers including Tcl/Tk, Java, and Python. VTK supports a
wide variety of visualization algorithms including scalar, vector,
tensor, texture, and volumetric methods. It also supports advanced
modeling techniques like implicit modeling, polygon reduction, mesh
smoothing, cutting, contouring, and Delaunay triangulation.  Moreover,
dozens of imaging algorithms have been integrated into the system.
This allows mixing 2D imaging / 3D graphics algorithms and data.

NOTE: The java wrapper is not included by default.  You may rebuild
      the srpm using "--with java" with JDK installed.

NOTE: All patented routines which are part of the package have been
      removed in this version.

%package devel
Summary:	VTK header files for building C++ code
Summary(pl):	Pliki nag³ówkowe VTK dla C++
Group:		Development/C++
Requires:	vtk

%description devel 
This provides the VTK header files required to compile C++
programs that use VTK to do 3D visualisation.

%package tcl
Summary:	Tcl bindings for VTK
Summary(pl):	Dowi±zania Tcl do VTK
Group:		System/Libraries
Requires:	vtk

%description tcl
The Visualization ToolKit (VTK) is an object oriented software system
for 3D computer graphics, image processing, and visualization. VTK
includes a textbook, a C++ class library, and several interpreted
interface layers including Tcl/Tk, Java, and Python. VTK supports a
wide variety of visualization algorithms including scalar, vector,
tensor, texture, and volumetric methods. It also supports advanced
modeling techniques like implicit modeling, polygon reduction, mesh
smoothing, cutting, contouring, and Delaunay triangulation.  Moreover,
dozens of imaging algorithms have been integrated into the system.
This allows mixing 2D imaging / 3D graphics algorithms and data.

This package contains tcl bindings for VTK.

%package python
Summary:	Python bindings for VTK
Summary(pl):	Dowi±zania Pythona do VTK
Requires:	vtk
Provides:	vtk
Group:		System/Libraries

%description python 
The Visualization ToolKit (VTK) is an object oriented software system
for 3D computer graphics, image processing, and visualization. VTK
includes a textbook, a C++ class library, and several interpreted
interface layers including Tcl/Tk, Java, and Python. VTK supports a
wide variety of visualization algorithms including scalar, vector,
tensor, texture, and volumetric methods. It also supports advanced
modeling techniques like implicit modeling, polygon reduction, mesh
smoothing, cutting, contouring, and Delaunay triangulation.  Moreover,
dozens of imaging algorithms have been integrated into the system.
This allows mixing 2D imaging / 3D graphics algorithms and data.

This package contains python bindings for VTK.

%package java
Summary:	Java bindings for VTK
Summary(pl):	Dowi±zania Javy do VTK
Group:		Development/Java
Requires:	vtk

%description java
The Visualization ToolKit (VTK) is an object oriented software system
for 3D computer graphics, image processing, and visualization. VTK
includes a textbook, a C++ class library, and several interpreted
interface layers including Tcl/Tk, Java, and Python. VTK supports a
wide variety of visualization algorithms including scalar, vector,
tensor, texture, and volumetric methods. It also supports advanced
modeling techniques like implicit modeling, polygon reduction, mesh
smoothing, cutting, contouring, and Delaunay triangulation.  Moreover,
dozens of imaging algorithms have been integrated into the system.
This allows mixing 2D imaging / 3D graphics algorithms and data.

This package contains java bindings for VTK.

%package examples
Summary:	C++, Tcl and Python example programs/scripts for VTK
Summary(pl):	Przyk³adowe programy/skrypty w C++, Tcl-u i Pythonie dla VTK
Group:		Development/Other
Requires:	vtk
Requires:	vtk-data

%description examples
This package contains all the examples from the VTK source.
To compile the C++ examples you will need to install the vtk-devel
package as well. The Python and Tcl examples can be run with the
corresponding packages (vtk-python, vtk-tcl).

%package test-suite
Summary:	Test programs for VTK
Summary(pl):	Programy testowe dla VTK
Group:		Development/Other
Requires:	vtk
Requires:	vtk-data

%description test-suite
This package contains all testing programs from the VTK source. The
source code of these programs can be found in the vtk-examples
package.

%package data
Summary:	Data files for VTK
Summary(pl):	Pliki danych dla VTK
Group:		Development/Libraries

%description data 
This package contains all the data from the VTKData repository. These
data are required to run various examples from the examples package.

%prep
%setup -q -a 1 -n VTK-%version
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
        -DLIBRARY_OUTPUT_PATH:PATH=$RPM_BUILD_DIR/VTK-%version/lib \
        -DEXECUTABLE_OUTPUT_PATH:PATH=$RPM_BUILD_DIR/VTK-%version/bin  \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
 	-DBUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_DOCUMENTATION:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-DCMAKE_BACKWARDS_COMPATIBILITY=1.8 \
	-DOPENGL_INCLUDE_PATH:PATH=/usr/X11R6/include/GL \
	-DPYTHON_INCLUDE_PATH:PATH=%{_includedir}/python2.3 \
	-DPYTHON_LIBRARY:FILEPATH=$(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'lib', 'python' + sys.version        [:3], 'config/libpython' + sys.version[:3] + '.a')") \
	-DPYTHON_UTIL_LIBRARY:PATH=/usr/lib/libutil.so \
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
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/gtk
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/qt
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/testing
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/tk
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/util
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk/wx
install -d -m 755 $RPM_BUILD_ROOT/$VTKPYTHONPATH
install -d -m 755 $RPM_BUILD_ROOT/usr/include/vtk

#install libs and tcl
#%makeinstall_std
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT%{_libdir}/vtk/*.so
for f in $RPM_BUILD_ROOT%{_libdir}/vtk/libvtk*Python*.so
do
  ln -s ../`basename $f` $RPM_BUILD_ROOT%{_libdir}/vtk/python/
done

#install binaries
install  -m 755 bin/* $RPM_BUILD_ROOT%{_bindir}

#install python
install  -m 644 Wrapping/Python/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python
install  -m 644 Wrapping/Python/vtk/*.py $RPM_BUILD_ROOT%{_libdir}/vtk/python/vtk
install  -m 644 Wrapping/Python/vtk/gtk/*.py $RPM_BUILD_ROOT/usr/lib/vtk/python/vtk/gtk
install  -m 644 Wrapping/Python/vtk/qt/*.py $RPM_BUILD_ROOT/usr/lib/vtk/python/vtk/qt
install  -m 644 Wrapping/Python/vtk/tk/*.py $RPM_BUILD_ROOT/usr/lib/vtk/python/vtk/tk
install  -m 644 Wrapping/Python/vtk/util/*.py $RPM_BUILD_ROOT/usr/lib/vtk/python/vtk/util
install  -m 644 Wrapping/Python/vtk/wx/*.py $RPM_BUILD_ROOT/usr/lib/vtk/python/vtk/wx
cat > $RPM_BUILD_ROOT/$VTKPYTHONPATH/vtkpython.pth <<_EOF
%{_libdir}/vtk/python
_EOF

%if %build_java
#install java
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/vtk/java
install  -m 644 lib/vtk.jar     $RPM_BUILD_ROOT/usr/lib/vtk/java
install  -m 644 java/vtk/*.java $RPM_BUILD_ROOT%{_libdir}/vtk/java
%endif

#install data
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name-data
cp -r VTKData-release-4-2/* $RPM_BUILD_ROOT/%_datadir/%name-data
rm -fr $RPM_BUILD_ROOT/%_datadir/%name-data/CVS

#install test-suite and examples
for d in Common Filtering Graphics Hybrid IO Imaging Parallel Patented Rendering
do
	mkdir -p $RPM_BUILD_ROOT/%_datadir/vtk-examples/Testing/$d
	cp -a $d/Testing/* $RPM_BUILD_ROOT/%_datadir/vtk-examples/Testing/$d
done
cp -a Examples $RPM_BUILD_ROOT/%_datadir/vtk-examples

# get rid of unwanted files
find $RPM_BUILD_ROOT/%_datadir/vtk-examples -name "*.o" -exec rm {} \;
find $RPM_BUILD_ROOT/%_datadir/vtk-examples -name CMakeCache.txt -exec rm {} \;
find $RPM_BUILD_ROOT/%_datadir/vtk-examples -name Makefile -exec rm {} \;
find $RPM_BUILD_ROOT/%_datadir/vtk-examples -name DartTestfile.txt -exec rm {} \;
find $RPM_BUILD_ROOT/%_datadir/vtk-examples -name .NoDartCoverage -exec rm {} \;
find $RPM_BUILD_ROOT/%_datadir/vtk-examples -name "CMake*" -exec rm {} \;
find $RPM_BUILD_ROOT/%_datadir/vtk-examples -name "cmake.*" -exec rm {} \;

# Generate the package testing-progs lists and store them in file-lists
echo "%defattr (-, root, root)" > testing-progs-list
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

%post -p /sbin/ldconfig
%post tcl -p /sbin/ldconfig
%post python -p /sbin/ldconfig
%if %build_java
%post java -p /sbin/ldconfig
%endif

%postun -p /sbin/ldconfig
%postun tcl -p /sbin/ldconfig
%postun python -p /sbin/ldconfig 
%if %build_java
%postun java -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README.html vtkLogo.jpg
%dir %{_libdir}/vtk
%{_libdir}/vtk/libvtkCommon.so 
%{_libdir}/vtk/libvtkFiltering.so 
%{_libdir}/vtk/libvtkGraphics.so
%{_libdir}/vtk/libvtkHybrid.so
%{_libdir}/vtk/libvtkImaging.so
%{_libdir}/vtk/libvtkIO.so
%{_libdir}/vtk/libvtkParallel.so
%{_libdir}/vtk/libvtkRendering.so
%{_libdir}/vtk/libvtkjpeg.so 
%{_libdir}/vtk/libvtkpng.so 
%{_libdir}/vtk/libvtkzlib.so
%{_libdir}/vtk/libvtkexpat.so
%{_libdir}/vtk/libvtkfreetype.so
%{_libdir}/vtk/libvtkftgl.so
%{_libdir}/vtk/libvtktiff.so

%files devel
%defattr(-,root,root)
%doc %{_libdir}/vtk/doxygen
%{_includedir}/vtk
%{_libdir}/vtk/CMake
%{_libdir}/vtk/*.cmake
%doc Utilities/Upgrading/*

%files test-suite -f testing-progs-list

%files tcl
%defattr(-,root,root)
%{_bindir}/vtkWrapTcl
%{_libdir}/vtk/libvtk*TCL.so 
%{_bindir}/vtk
%{_libdir}/vtk/tcl
%dir %{_libdir}/vtk/testing
%{_libdir}/vtk/testing/*.tcl
%doc README.html 
%doc vtkLogo.jpg

%files python
%defattr(-,root,root)
%_bindir/vtkWrapPython
%_bindir/vtkpython
%_libdir/vtk/libvtk*Python*.so 
%_libdir/vtk/python
%dir %_libdir/vtk/testing
%_libdir/vtk/testing/*.py
%(python -c"import os,sys; print os.path.join(sys.exec_prefix, 'lib', 'python' + sys.version[:3],'site-packages', 'vtkpython.pth')")

%if %build_java
%files java
%defattr(-,root,root)
%{_bindir}/vtkParseJava
%{_bindir}/vtkWrapJava
%{_bindir}/VTKJavaExecutable
%{_libdir}/vtk/libvtk*Java.so 
%{_libdir}/vtk/java
%endif

%files examples
%defattr(-,root,root)
%dir %_datadir/vtk-examples
%_datadir/vtk-examples/Examples
%_datadir/vtk-examples/Testing

%files data
%defattr(-,root,root)
%dir %_datadir/vtk-data
%_datadir/vtk-data/Baseline
%_datadir/vtk-data/Data
%_datadir/vtk-data/VTKData.readme

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Mar 01 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.2.2-4mdk
- Own dir (again)

* Sun Feb 29 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.2.2-3mdk
- Own dir

* Sat Aug 9 2003 Austin Acton <aacton@yorku.ca> 4.2.2-2mdk
- python 2.3

* Thu Jul 17 2003 Austin Acton <aacton@yorku.ca> 4.2.2-1mdk
- 4.2.2
- some DIRM
- some removal of some lint
- some java conditionals

* Sun Feb 2 2003 Austin Acton <aacton@yorku.ca> 4.0-1mdk
- initial package
- stole most of specfile from http://www.creatis.insa-lyon.fr/vtk/
