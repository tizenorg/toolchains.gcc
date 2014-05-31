# Combined gcc / cross-armv*-gcc(-accel) specfile
Name: gcc

# crossbuild / accelerator section
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
%define crossbuild 0
%define accelerator_crossbuild 0
%if "%{name}" != "gcc"
# this is the ix86 -> arm cross compiler (cross-armv*-gcc)
#
# cross arch retrieval
%define crossarch %(echo %{name} | sed -e "s/cross-\\(.*\\)-gcc/\\1/")
# We set requires/provides by hand and disable post-build-checks.
# Captain Trunk: Sledge, you cannot disarm that nuclear bomb!
# Sledge Hammer: Trust me, I know what I'm doing.
AutoReqProv: 0
AutoReq: false
#!BuildIgnore: rpmlint-Moblin rpmlint-mini post-build-checks
# cross platform
%define cross_gcc_target_platform %{crossarch}-tizen-linux-gnueabi
# gcc_target_platform holds the host (executing the compiler)
# cross_gcc_target_platform holds the target (for which the compiler is producing binaries)
# prefix for cross compiler
%define _prefix /opt/cross
# strip of 'foreign arch' symbols fails
%define __strip /bin/true
# sysroot for cross-compiler
%define crosssysroot %{_prefix}/%{cross_gcc_target_platform}/sys-root
# flag
%define crossbuild 1
# macros in buildrequires is hard to expand for the scheduler (e.g. crossarch) which would make this easier.
#BuildRequires: cross-%{crossarch}-eglibc cross-%{crossarch}-glibc-devel cross-%{crossarch}-glibc-headers
#BuildRequires: cross-%{crossarch}-kernel-headers cross-%{crossarch}-binutils
# Fixme: find way to make this without listing every package
%if "%{name}" == "cross-armv5tel-gcc"
BuildRequires: cross-armv5tel-eglibc cross-armv5tel-eglibc-devel cross-armv5tel-eglibc-headers
BuildRequires: cross-armv5tel-kernel-headers cross-armv5tel-binutils
%define crossextraconfig %{nil}
%endif
%if "%{name}" == "cross-armv6l-gcc"
BuildRequires: cross-armv6l-eglibc cross-armv6l-eglibc-devel cross-armv6l-eglibc-headers
BuildRequires: cross-armv6l-kernel-headers cross-armv6l-binutils
%define crossextraconfig %{nil}
%endif
%if "%{name}" == "cross-armv7l-gcc"
BuildRequires: cross-armv7l-eglibc cross-armv7l-eglibc-devel cross-armv7l-eglibc-headers
BuildRequires: cross-armv7l-kernel-headers cross-armv7l-binutils
%define crossextraconfig --with-float=softfp --with-fpu=vfpv3 --with-arch=armv7-a
%endif
%if "%{name}" == "cross-armv7hl-gcc"
BuildRequires: cross-armv7hl-eglibc cross-armv7hl-eglibc-devel cross-armv7hl-eglibc-headers
BuildRequires: cross-armv7hl-kernel-headers cross-armv7hl-binutils
%define crossextraconfig --with-float=hard --with-fpu=vfpv3-d16 --with-arch=armv7-a
%endif
%if "%{name}" == "cross-armv7nhl-gcc"
BuildRequires: cross-armv7nhl-eglibc cross-armv7nhl-eglibc-devel cross-armv7nhl-eglibc-headers
BuildRequires: cross-armv7nhl-kernel-headers cross-armv7nhl-binutils
%define crossextraconfig --with-float=hard --with-fpu=neon --with-arch=armv7-a
%endif
# Fixme: see above
%if "%{name}" == "cross-armv5tel-gcc-accel"
BuildRequires: cross-armv5tel-eglibc cross-armv5tel-eglibc-devel cross-armv5tel-eglibc-headers
BuildRequires: cross-armv5tel-kernel-headers cross-armv5tel-binutils
%define crossextraconfig %{nil}
%endif
%if "%{name}" == "cross-armv6l-gcc-accel"
BuildRequires: cross-armv6l-eglibc cross-armv6l-eglibc-devel cross-armv6l-eglibc-headers
BuildRequires: cross-armv6l-kernel-headers cross-armv6l-binutils
%define crossextraconfig %{nil}
%endif
%if "%{name}" == "cross-armv7l-gcc-accel"
BuildRequires: cross-armv7l-eglibc cross-armv7l-eglibc-devel cross-armv7l-eglibc-headers
BuildRequires: cross-armv7l-kernel-headers cross-armv7l-binutils
%define crossextraconfig --with-float=softfp --with-fpu=vfpv3 --with-arch=armv7-a
%endif
%if "%{name}" == "cross-armv7hl-gcc-accel"
BuildRequires: cross-armv7hl-eglibc cross-armv7hl-eglibc-devel cross-armv7hl-eglibc-headers
BuildRequires: cross-armv7hl-kernel-headers cross-armv7hl-binutils
%define crossextraconfig --with-float=hard --with-fpu=vfpv3-d16 --with-arch=armv7-a
%endif
%if "%{name}" == "cross-armv7nhl-gcc-accel"
BuildRequires: cross-armv7nhl-eglibc cross-armv7nhl-eglibc-devel cross-armv7nhl-eglibc-headers
BuildRequires: cross-armv7nhl-kernel-headers cross-armv7nhl-binutils
%define crossextraconfig --with-float=hard --with-fpu=neon --with-arch=armv7-a
%endif
# single target atm.
ExclusiveArch: %ix86
#
# special handling for Tizen ARM build acceleration
# cross-armv*-gcc-accel
%if "%(echo %{name} | sed -e "s/cross-.*-gcc-\\(.*\\)/\\1/")" == "accel"
# cross architecture
%define crossarch %(echo %{name} | sed -e "s/cross-\\(.*\\)-gcc-accel/\\1/")
# cross target platform
%define cross_gcc_target_platform %{crossarch}-tizen-linux-gnueabi
# prefix - as it's going to "replace" the original compiler ...
%define _prefix /usr
# cross-build sets sysroot as default , we need to override this a bit
%define crosssysroot /
# where to find the libs during the build
%define crossbuildsysroot /opt/cross/%{cross_gcc_target_platform}/sys-root
# flags
%define crossbuild 1
%define accelerator_crossbuild 1
# where to find the libs at runtime
%define newrpath /emul/ia32-linux/lib:/emul/ia32-linux/usr/lib
%define _build_name_fmt    %%{ARCH}/%%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.dontuse.rpm
%endif
# end special accel
%endif
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# end crossbuild / accelerator section

%global gcc_version 4.6
%global gcc_release 2013.05
%global _unpackaged_files_terminate_build 0
%ifarch %{arm}
%global build_cloog 0
%else
%if %{crossbuild}
%global build_cloog 0
%else
%global build_cloog 1
%endif
%endif
%global multilib_64_archs x86_64
%ifarch x86_64
%global multilib_32_arch i686
%endif

Summary: Various compilers (C, C++, Objective-C, Java, ...)
Version: %{gcc_version}
Release: %{gcc_release}
VCS:     toolchains/gcc#submit/master/20131126.022252-0-ga6b8565e99e42d6caee61b5015810d8b78c511bf
License: GPLv3+, GPLv3+ with exceptions and GPLv2+ with exceptions
Group: Development/Languages
URL: http://gcc.gnu.org
Source0: gcc-linaro-%{version}-%{gcc_release}.tar.xz
Source1: libgcc_post_upgrade.c
Source100: gcc-rpmlintrc
Source200: baselibs.conf
Source300: precheckin.sh
Source301: aaa_README.PACKAGER

BuildRequires: binutils >= 2.19.51.0.14
BuildRequires: eglibc-devel >= 2.4.90-13
BuildRequires: eglibc-static
BuildRequires: zlib-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: mpc-devel
BuildRequires: elfutils-devel >= 0.72
%if %{build_cloog}
BuildRequires: ppl >= 0.10, ppl-devel >= 0.10, cloog-ppl >= 0.15, cloog-ppl-devel >= 0.15
%endif

Requires: cpp = %{version}-%{release}
Requires: libgcc >= %{version}-%{release}
Requires: libgomp = %{version}-%{release}
Requires: eglibc-devel
Requires: binutils >= 2.19.51.0.14

%if !%{crossbuild}
Obsoletes: gcc < %{version}-%{release}
AutoReq: true
# /!crossbuild
%endif

Patch41: libgcc_post_upgrade.c.arm.patch

#We need -gnueabi indicator for ARM
%ifnarch %{arm}
%global _gnu %{nil}
%endif
%global gcc_target_platform %{_target_platform}

%description
The gcc package contains the GNU Compiler Collection version 4.5.0.
You'll need this package in order to compile C code.

%package -n libgcc
Summary: GCC version 4.5.0 shared support library
Group: System Environment/Libraries
Obsoletes: libgcc < %{version}-%{release}
Obsoletes: libgcc43
Autoreq: false

%description -n libgcc
This package contains GCC shared support library which is needed
e.g. for exception handling support.

%package c++
Summary: C++ support for GCC
Group: Development/Languages
Requires: gcc = %{version}-%{release}
Requires: libstdc++ = %{version}-%{release}
Requires: libstdc++-devel = %{version}-%{release}
Obsoletes: gcc-c++ < %{version}-%{release}
Obsoletes: gcc43-c++
Autoreq: true

%description c++
This package adds C++ support to the GNU Compiler Collection.
It includes support for most of the current C++ specification,
including templates and exception handling.

%package -n libstdc++
Summary: GNU Standard C++ Library
Group: System Environment/Libraries
Obsoletes: libstdc++ < %{version}-%{release}
Obsoletes: libstdc++43
Obsoletes: libstdc++6 < %{version}-%{release}
Autoreq: true
Requires: eglibc

%description -n libstdc++
The libstdc++ package contains a rewritten standard compliant GCC Standard
C++ Library.

%package -n libstdc++-devel
Summary: Header files and libraries for C++ development
Group: Development/Libraries
Requires: libstdc++ = %{version}-%{release}
Obsoletes: libstdc++-devel < %{version}-%{release}
Obsoletes: libstdc++43-devel
Autoreq: true

%description -n libstdc++-devel
This is the GNU implementation of the standard C++ libraries.  This
package includes the header files and libraries needed for C++
development. This includes rewritten implementation of STL.

%package -n libstdc++-docs
Summary: Documentation for the GNU standard C++ library
Group: Development/Libraries
Obsoletes: libstdc++-docs < %{version}-%{release}
Obsoletes: libstdc++43-doc
Autoreq: true

%description -n libstdc++-docs
Manual, doxygen generated API information and Frequently Asked Questions
for the GNU standard C++ library.

%package -n libgomp
Summary: GCC OpenMP v3.0 shared support library
Group: System Environment/Libraries
Obsoletes: libgomp < %{version}-%{release}
Obsoletes: libgomp43

%description -n libgomp
This package contains GCC shared support library which is needed
for OpenMP v3.0 support.

%package -n libmudflap
Summary: GCC mudflap shared support library
Group: System Environment/Libraries

%description -n libmudflap
This package contains GCC shared support library which is needed
for mudflap support.

%package -n libmudflap-devel
Summary: GCC mudflap support
Group: Development/Libraries
Requires: libmudflap = %{version}-%{release}
Requires: gcc = %{version}-%{release}

%description -n libmudflap-devel
This package contains headers and static libraries for building
mudflap-instrumented programs.

To instrument a non-threaded program, add -fmudflap
option to GCC and when linking add -lmudflap, for threaded programs
also add -fmudflapth and -lmudflapth.


%package -n cpp
Summary: The C Preprocessor
Group: Development/Languages
Requires: mpc
Obsoletes: cpp < %{version}-%{release}
Obsoletes: cpp43
Autoreq: true

%description -n cpp
Cpp is the GNU C-Compatible Compiler Preprocessor.
Cpp is a macro processor which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define macros, abbreviations for longer
constructs.

The C preprocessor provides four separate functionalities: the
inclusion of header files (files of declarations that can be
substituted into your program); macro expansion (you can define macros,
and the C preprocessor will replace the macros with their definitions
throughout the program); conditional compilation (using special
preprocessing directives, you can include or exclude parts of the
program according to various conditions); and line control (if you use
a program to combine or rearrange source files into an intermediate
file which is then compiled, you can use line control to inform the
compiler about where each source line originated).

You should install this package if you are a C programmer and you use
macros.

%package -n gcc-multilib
Summary: for 64bit multilib support
Group: System Environment/Libraries
Autoreq: true

%description -n gcc-multilib
This is one set of libraries which support 64bit multilib on top of
32bit enviroment from compiler side.

%prep
%setup -q -n gcc-linaro-%{version}-%{gcc_release}

echo '%{version}' >gcc/BASE-VER

cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

%build
rm -fr obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
cd obj-%{gcc_target_platform}


CC=gcc
OPT_FLAGS=`echo %{optflags}|sed -e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[12]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
case "$OPT_FLAGS" in
  *-fasynchronous-unwind-tables*)
    sed -i -e 's/-fno-exceptions /-fno-exceptions -fno-asynchronous-unwind-tables/' \
      ../gcc/Makefile.in
    ;;
esac

%ifarch %arm
# gcc 45 segfaults on O2g.gch generation. (cc1plus)
%define ARM_EXTRA_CONFIGURE --disable-libstdcxx-pch
# for armv7hl reset the gcc specs
%ifarch armv7hl
%define ARM_EXTRA_CONFIGURE --disable-libstdcxx-pch --with-float=hard --with-fpu=vfpv3-d16 --with-arch=armv7-a
%endif
# for armv7nhl reset the gcc specs
%ifarch armv7nhl
%define ARM_EXTRA_CONFIGURE --disable-libstdcxx-pch --with-float=hard --with-fpu=neon --with-arch=armv7-a
%endif
%endif

%if %{crossbuild}
# cross build
export PATH=/opt/cross/bin:$PATH
# strip all after -march . no arch specific options in cross-compiler build .
# -march=core2 -mssse3 -mtune=atom -mfpmath=sse -fasynchronous-unwi
export OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e "s#\-march=.*##g"`
%if %{accelerator_crossbuild}
# adding -rpath to the special crosscompiler
export OPT_FLAGS="$OPT_FLAGS -Wl,-rpath,/emul/ia32-linux/usr/lib:/emul/ia32-linux/lib:/usr/lib:/lib"
%endif
%endif

CC="$CC" CFLAGS="$OPT_FLAGS" CXXFLAGS="`echo $OPT_FLAGS | sed 's/ -Wall / /g'`" XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
	--enable-shared --enable-linker-build-id \
%ifarch %{arm}
	--enable-checking=release \
	--disable-sjlj-exceptions \
	%ARM_EXTRA_CONFIGURE \
%else
%if %{crossbuild}
	--build=%{gcc_target_platform} \
	--host=%{gcc_target_platform} \
	--target=%{cross_gcc_target_platform} \
	--disable-checking \
%else
	--enable-checking=release \
	--enable-multiarch \
%endif
%endif
%if %{build_cloog}
	--with-ppl --with-cloog \
        --disable-ppl-version-check \
        --enable-cloog-backend=ppl \
%endif
	--with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions \
	--enable-gnu-unique-object --enable-lto \
	--without-included-gettext \
	--enable-threads=posix \
	--enable-nls \
	--disable-bootstrap \
	--enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes \
	--enable-plugin --enable-gold --enable-ld=default --with-plugin-ld=ld.gold \
	--enable-languages=c,c++ \
	--disable-libgcj \
%if !%{crossbuild}
%ifarch %{ix86} x86_64
	--with-tune=generic \
%endif
%ifarch %{ix86}
	--with-arch=i686 \
%endif
%ifarch x86_64
	--with-arch_32=i686 \
%endif
	--build=%{gcc_target_platform}  || ( cat config.log ; exit 1 )
#end for x86
%else
%if !%{accelerator_crossbuild}
	%{crossextraconfig} \
	--with-sysroot=%{crosssysroot}
#end for cross-compiler
%else
	%{crossextraconfig} \
	--program-transform-name='s/%{cross_gcc_target_platform}-//' \
	--with-gxx-include-dir=%{_prefix}/include/c++/%{gcc_version} \
	--with-build-sysroot=%{crossbuildsysroot} \
	--with-sysroot=%{crosssysroot}
#end for special cross-compiler
%endif
%endif

make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS"


# Make generated man pages even if Pod::Man is not new enough
perl -pi -e 's/head3/head2/' ../contrib/texi2pod.pl
for i in ../gcc/doc/*.texi; do
  cp -a $i $i.orig; sed 's/ftable/table/' $i.orig > $i
done
make -C gcc generated-manpages
for i in ../gcc/doc/*.texi; do mv -f $i.orig $i; done
cd ..


%install
rm -fr %{buildroot}

mkdir -p %{buildroot}/usr/share/license
cp gcc/COPYING %{buildroot}/usr/share/license/gcc
cp gcc/COPYING %{buildroot}/usr/share/license/cpp
cp gcc/COPYING %{buildroot}/usr/share/license/libgcc
cp gcc/COPYING %{buildroot}/usr/share/license/gcc-c++
cp gcc/COPYING %{buildroot}/usr/share/license/libstdc++
cp gcc/COPYING %{buildroot}/usr/share/license/libgomp
cp gcc/COPYING %{buildroot}/usr/share/license/libmudflap

cd obj-%{gcc_target_platform}

%if !%{crossbuild}
# native
TARGET_PLATFORM=%{gcc_target_platform}
# There are some MP bugs in libstdc++ Makefiles
make -C %{gcc_target_platform}/libstdc++-v3
%else
# cross build
export PATH=/opt/cross/bin:$PATH
# strip all after -march . no arch specific options in cross-compiler build .
# -march=core2 -mssse3 -mtune=atom -mfpmath=sse -fasynchronous-unwi
export OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e "s#\-march=.*##g"`
#echo "$OPT_FLAGS"
#TARGET_PLATFORM=%{cross_gcc_target_platform}
# There are some MP bugs in libstdc++ Makefiles
#make -C %{cross_gcc_target_platform}/libstdc++-v3
%endif

make DESTDIR=%{buildroot} install
#prefix=%{buildroot}%{_prefix} mandir=%{buildroot}%{_mandir} \
#  infodir=%{buildroot}%{_infodir} install

%if !%{crossbuild}
# native
# \/\/\/

FULLPATH=%{buildroot}%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
FULLEPATH=%{buildroot}%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}

ln -sf gcc %{buildroot}%{_prefix}/bin/cc
mkdir -p %{buildroot}/lib
ln -sf ..%{_prefix}/bin/cpp %{buildroot}/lib/cpp
rm -f %{buildroot}%{_infodir}/dir
gzip -9 %{buildroot}%{_infodir}/*.info*

cxxconfig="`find %{gcc_target_platform}/libstdc++-v3/include -name c++config.h`"
for i in `find %{gcc_target_platform}/[36]*/libstdc++-v3/include -name c++config.h 2>/dev/null`; do
  if ! diff -up $cxxconfig $i; then
    cat > %{buildroot}%{_prefix}/include/c++/%{gcc_version}/%{gcc_target_platform}/bits/c++config.h <<EOF
#ifndef _CPP_CPPCONFIG_WRAPPER
#define _CPP_CPPCONFIG_WRAPPER 1
#include <bits/wordsize.h>
#if __WORDSIZE == 32
%ifarch %{multilib_64_archs}
`cat $(find %{gcc_target_platform}/32/libstdc++-v3/include -name c++config.h)`
%else
`cat $(find %{gcc_target_platform}/libstdc++-v3/include -name c++config.h)`
%endif
#else
%ifarch %{multilib_64_archs}
`cat $(find %{gcc_target_platform}/libstdc++-v3/include -name c++config.h)`
%else
`cat $(find %{gcc_target_platform}/64/libstdc++-v3/include -name c++config.h)`
%endif
#endif
#endif
EOF
    break
  fi
done

for f in `find %{buildroot}%{_prefix}/include/c++/%{gcc_version}/%{gcc_target_platform}/ -name c++config.h`; do
  for i in 1 2 4 8; do
    sed -i -e 's/#define _GLIBCXX_ATOMIC_BUILTINS_'$i' 1/#ifdef __GCC_HAVE_SYNC_COMPARE_AND_SWAP_'$i'\
&\
#endif/' $f
  done
done

# Nuke bits/stdc++.h.gch dirs
# 1) there is no bits/stdc++.h header installed, so when gch file can't be
#    used, compilation fails
# 2) sometimes it is hard to match the exact options used for building
#    libstdc++-v3 or they aren't desirable
# 3) there are multilib issues, conflicts etc. with this
# 4) it is huge
# People can always precompile on their own whatever they want, but
# shipping this for everybody is unnecessary.
rm -rf %{buildroot}%{_prefix}/include/c++/%{gcc_version}/%{gcc_target_platform}/bits/stdc++.h.gch


if [ -n "$FULLLPATH" ]; then
  mkdir -p $FULLLPATH
else
  FULLLPATH=$FULLPATH
fi

find %{buildroot} -name \*.la | xargs rm -f

mkdir -p %{buildroot}/%{_lib}
mv -f %{buildroot}%{_prefix}/%{_lib}/libgcc_s.so.1 %{buildroot}/%{_lib}/libgcc_s-%{gcc_version}.so.1
chmod 755 %{buildroot}/%{_lib}/libgcc_s-%{gcc_version}.so.1
ln -sf libgcc_s-%{gcc_version}.so.1 %{buildroot}/%{_lib}/libgcc_s.so.1
ln -sf /%{_lib}/libgcc_s.so.1 %{buildroot}/%{_libdir}/libgcc_s.so
ln -sf /%{_lib}/libgcc_s.so.1 $FULLPATH/libgcc_s.so
%ifarch %{multilib_64_archs}
ln -sf /lib/libgcc_s.so.1 $FULLPATH/32/libgcc_s.so
%endif

mv -f %{buildroot}%{_prefix}/%{_lib}/libgomp.spec $FULLPATH/

mkdir -p %{buildroot}%{_prefix}/libexec/getconf
if gcc/xgcc -B gcc/ -E -dD -xc /dev/null | grep __LONG_MAX__.*2147483647; then
  ln -sf POSIX_V6_ILP32_OFF32 %{buildroot}%{_prefix}/libexec/getconf/default
else
  ln -sf POSIX_V6_LP64_OFF64 %{buildroot}%{_prefix}/libexec/getconf/default
fi


mkdir -p %{buildroot}%{_datadir}/gdb/auto-load/%{_prefix}/%{_lib}
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++*gdb.py* \
      %{buildroot}%{_datadir}/gdb/auto-load/%{_prefix}/%{_lib}/

pushd $FULLPATH
if [ "%{_lib}" = "lib" ]; then
ln -sf ../../../libstdc++.so.6.* libstdc++.so
ln -sf ../../../libgomp.so.1.* libgomp.so
ln -sf ../../../libmudflap.so.0.* libmudflap.so
ln -sf ../../../libmudflapth.so.0.* libmudflapth.so
else
ln -sf ../../../../%{_lib}/libstdc++.so.6.* libstdc++.so
ln -sf ../../../../%{_lib}/libgomp.so.1.* libgomp.so
ln -sf ../../../../%{_lib}/libmudflap.so.0.* libmudflap.so
ln -sf ../../../../%{_lib}/libmudflapth.so.0.* libmudflapth.so
fi
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libsupc++.*a .
mv -f %{buildroot}%{_prefix}/%{_lib}/libgomp.*a .
mv -f %{buildroot}%{_prefix}/%{_lib}/libmudflap{,th}.*a $FULLLPATH/

%ifarch %{multilib_64_archs}
mkdir -p 32
ln -sf ../`echo ../../../../lib64/libstdc++.so.6.* | sed s~/../lib64/~/~` 32/libstdc++.so
ln -sf ../`echo ../../../../lib64/libgomp.so.1.* | sed s~/../lib64/~/~` 32/libgomp.so
rm -f libmudflap.so libmudflapth.so
echo 'INPUT ( %{_prefix}/lib64/'`echo ../../../../lib64/libmudflap.so.0.* | sed 's,^.*libm,libm,'`' )' > libmudflap.so
echo 'INPUT ( %{_prefix}/lib64/'`echo ../../../../lib64/libmudflapth.so.0.* | sed 's,^.*libm,libm,'`' )' > libmudflapth.so
echo 'INPUT ( %{_prefix}/lib/'`echo ../../../../lib64/libmudflap.so.0.* | sed 's,^.*libm,libm,'`' )' > 32/libmudflap.so
echo 'INPUT ( %{_prefix}/lib/'`echo ../../../../lib64/libmudflapth.so.0.* | sed 's,^.*libm,libm,'`' )' > 32/libmudflapth.so
mv -f %{buildroot}%{_prefix}/lib/libsupc++.*a 32/
mv -f %{buildroot}%{_prefix}/lib/libgomp.*a 32/
ln -sf ../../../%{multilib_32_arch}-%{_vendor}-%{_target_os}/%{gcc_version}/libstdc++.a 32/libstdc++.a
ln -sf ../../../%{multilib_32_arch}-%{_vendor}-%{_target_os}/%{gcc_version}/libmudflap.a 32/libmudflap.a
ln -sf ../../../%{multilib_32_arch}-%{_vendor}-%{_target_os}/%{gcc_version}/libmudflapth.a 32/libmudflapth.a
%endif

# Strip debug info from Fortran/ObjC/Java static libraries
strip -g `find . \( -name libgomp.a \
		    -o -name libmudflap.a -o -name libmudflapth.a \
		    -o -name libgcc.a -o -name libgcov.a \) -a -type f`
popd
chmod 755 %{buildroot}%{_prefix}/%{_lib}/libgomp.so.1.*
chmod 755 %{buildroot}%{_prefix}/%{_lib}/libmudflap{,th}.so.0.*

mv $FULLPATH/include-fixed/syslimits.h $FULLPATH/include/syslimits.h
mv $FULLPATH/include-fixed/limits.h $FULLPATH/include/limits.h
for h in `find $FULLPATH/include -name \*.h`; do
  if grep -q 'It has been auto-edited by fixincludes from' $h; then
    rh=`grep -A2 'It has been auto-edited by fixincludes from' $h | tail -1 | sed 's|^.*"\(.*\)".*$|\1|'`
    diff -up $rh $h || :
    rm -f $h
  fi
done

cat > %{buildroot}%{_prefix}/bin/c89 <<"EOF"
#!/bin/sh
fl="-std=c89"
for opt; do
  case "$opt" in
    -ansi|-std=c89|-std=iso9899:1990) fl="";;
    -std=*) echo "`basename $0` called with non ANSI/ISO C option $opt" >&2
	    exit 1;;
  esac
done
exec gcc $fl ${1+"$@"}
EOF
cat > %{buildroot}%{_prefix}/bin/c99 <<"EOF"
#!/bin/sh
fl="-std=c99"
for opt; do
  case "$opt" in
    -std=c99|-std=iso9899:1999) fl="";;
    -std=*) echo "`basename $0` called with non ISO C99 option $opt" >&2
	    exit 1;;
  esac
done
exec gcc $fl ${1+"$@"}
EOF
chmod 755 %{buildroot}%{_prefix}/bin/c?9

mkdir -p %{buildroot}%{_prefix}/sbin
%ifarch %{arm}
patch %{SOURCE1} < %{PATCH41}
%endif
gcc -static -Os %{SOURCE1} -o %{buildroot}%{_prefix}/sbin/libgcc_post_upgrade
strip %{buildroot}%{_prefix}/sbin/libgcc_post_upgrade

cd ..

# Remove binaries we will not be including, so that they don't end up in
# gcc-debuginfo
rm -f %{buildroot}%{_prefix}/%{_lib}/{libffi*,libiberty.a}
rm -f $FULLEPATH/install-tools/{mkheaders,fixincl}
rm -f %{buildroot}%{_prefix}/lib/{32,64}/libiberty.a
%ifarch %{ix86} x86_64
%if !%{crossbuild}
rm -f %{buildroot}%{_prefix}/%{_lib}/libssp*
%endif
%endif

%ifarch %{multilib_64_archs}
# Remove libraries for the other arch on multilib arches
rm -f %{buildroot}%{_prefix}/lib/lib*.so*
rm -f %{buildroot}%{_prefix}/lib/lib*.a
%endif

# Rmove include-fixed
# /\/\/\
# native
%else
# cross
# \/\/\/
# additional install for cross
# remove some obsolete files
%if !%{accelerator_crossbuild}
#set -x
rm -rRf %buildroot/%{_prefix}/lib/libiberty.a
rm -rRf %buildroot/%{_prefix}/share
#set +x
%endif
# /\/\/\
# cross
%endif

%if !%{crossbuild}
# checking and split packaging for native ...
# native
# \/\/\/

%check
%if 0
cd obj-%{gcc_target_platform}

# run the tests.
make %{?_smp_mflags} -k check ALT_CC_UNDER_TEST=gcc ALT_CXX_UNDER_TEST=g++ RUNTESTFLAGS="--target_board=unix/'{,-fstack-protector}'" || :
echo ====================TESTING=========================
( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
echo ====================TESTING END=====================
mkdir testlogs-%{_target_platform}-%{version}-%{release}
for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats\|ada'`; do
  ln $i testlogs-%{_target_platform}-%{version}-%{release}/ || :
done
tar cf - testlogs-%{_target_platform}-%{version}-%{release} | bzip2 -9c \
  | uuencode testlogs-%{_target_platform}.tar.bz2 || :
rm -rf testlogs-%{_target_platform}-%{version}-%{release}

%endif

%clean
rm -rf %{buildroot}

%postun -p /sbin/ldconfig



%post -n libgcc -p %{_prefix}/sbin/libgcc_post_upgrade

%postun -n libgcc -p /sbin/ldconfig

%post -n libstdc++ -p /sbin/ldconfig

%postun -n libstdc++ -p /sbin/ldconfig

%postun -n libgomp -p /sbin/ldconfig

%post -n libmudflap -p /sbin/ldconfig

%postun -n libmudflap -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_prefix}/bin/cc
%{_prefix}/bin/c89
%{_prefix}/bin/c99
%{_prefix}/bin/gcc
%{_prefix}/bin/gcov
%ifnarch %{arm}
%{_prefix}/bin/%{gcc_target_platform}-gcc
%endif
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*
%{_mandir}/man7/*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include

# Shouldn't include all files under this fold, split to diff pkgs
#%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/*
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/lto1
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/lto-wrapper
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/collect2
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/liblto_plugin.*

%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/plugin
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/plugin/include
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/plugin/include/*

# Shouldn't include all files under this fold, split to diff pkgs
#%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/*
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stddef.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdarg.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdfix.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/varargs.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/float.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/limits.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdbool.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/iso646.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/syslimits.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/unwind.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/omp.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdint.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdint-gcc.h
%ifarch %{ix86} x86_64
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/emmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/pmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/tmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/ammintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/smmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/nmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/bmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/wmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/immintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/avxintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/x86intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/fma4intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/xopintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/lwpintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/abmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/popcntintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/ia32intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mm_malloc.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mm3dnow.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/cpuid.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/cross-stdarg.h
%endif

%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include-fixed
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include-fixed/README
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include-fixed/linux/a.out.h
# For ARM port
%ifarch %{arm}
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/arm_neon.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/ssp/ssp.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/ssp/stdio.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/ssp/string.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/ssp/unistd.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/stdfix.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/install-tools
%endif

%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/crt*.o
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgcc.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgcov.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgcc_eh.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgcc_s.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgomp.spec
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgomp.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libgomp.so
%ifarch %{multilib_64_archs}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/crt*.o
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libgcc.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libgcov.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libgcc_eh.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libgcc_s.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libgomp.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libgomp.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libmudflap.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libmudflapth.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libmudflap.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libmudflapth.so
%endif
%dir %{_prefix}/libexec/getconf
%{_prefix}/libexec/getconf/default
%doc gcc/README*  gcc/COPYING*
/usr/share/license/gcc
%manifest gcc.manifest

%files -n cpp
%defattr(-,root,root,-)
/lib/cpp
%{_prefix}/bin/cpp
%{_mandir}/man1/cpp.1*
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/cc1
/usr/share/license/cpp
%manifest cpp.manifest

%files -n libgcc
%defattr(-,root,root,-)
/%{_lib}/libgcc_s-%{gcc_version}.so.1
/%{_lib}/libgcc_s.*
/%{_libdir}/libgcc_s.*
%{_prefix}/sbin/libgcc_post_upgrade
%doc gcc/COPYING.LIB
/usr/share/license/libgcc
%manifest libgcc.manifest

# For ARM port
%ifarch %{arm}
%{_prefix}/%{_lib}/libssp*
%endif

%files c++
%defattr(-,root,root,-)
%ifnarch %{arm}
%{_prefix}/bin/%{gcc_target_platform}-*++
%endif
%{_prefix}/bin/g++
%{_prefix}/bin/c++
%{_mandir}/man1/g++.1*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_version}/cc1plus
%ifarch %{multilib_64_archs}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libstdc++.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libstdc++.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/32/libsupc++.a
%endif
%ifarch %{multilib_64_archs}
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libstdc++.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libsupc++.a
%endif
/usr/share/license/gcc-c++
%manifest gcc-c++.manifest

%files -n libstdc++
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libstdc++.*
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load/%{_prefix}
%dir %{_datadir}/gdb/auto-load/%{_prefix}/%{_lib}/
%{_datadir}/gdb/auto-load/%{_prefix}/%{_lib}/libstdc*gdb.py*
%dir %{_prefix}/share/gcc-%{gcc_version}
%{_prefix}/share/gcc-%{gcc_version}/python
/usr/share/license/libstdc++
%manifest libstdc++.manifest

%files -n libstdc++-devel
%defattr(-,root,root,-)
%dir %{_prefix}/include/c++
%dir %{_prefix}/include/c++/%{gcc_version}
%{_prefix}/include/c++/%{gcc_version}/[^gjos]*
%{_prefix}/include/c++/%{gcc_version}/os*
%{_prefix}/include/c++/%{gcc_version}/s[^u]*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libstdc++.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libsupc++.a
%ifnarch  %{multilib_64_archs}
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libstdc++.so
%endif

%files -n libgomp
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libgomp.*
/usr/share/license/libgomp
%manifest libgomp.manifest

%files -n libmudflap
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libmudflap.*
%{_prefix}/%{_lib}/libmudflapth.*
/usr/share/license/libmudflap
%manifest libmudflap.manifest

%files -n libmudflap-devel
%defattr(-,root,root,-)
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/include/mf-runtime.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libmudflap.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libmudflapth.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libmudflap.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}/libmudflapth.so

# /\/\/\
# native
%else
# cross
# \/\/\/
%files
/usr/share/license/gcc
%manifest gcc.manifest
%defattr(-,root,root,-)
%{_prefix}
# /\/\/\
# cross
%endif
