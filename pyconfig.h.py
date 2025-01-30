/* pyconfig.h.in.  Generated from configure.ac by autoheader.  */


#ifndef Py_PYCONFIG_H
#define Py_PYCONFIG_H


/* Define if building universal (internal helper macro) */
#undef AC_APPLE_UNIVERSAL_BUILD

/* BUILD_GNU_TYPE + AIX_BUILDDATE are used to construct the PEP425 tag of the
   build system. */
#undef AIX_BUILDDATE

/* Define for AIX if your compiler is a genuine IBM xlC/xlC_r and you want
   support for AIX C++ shared extension modules. */
#undef AIX_GENUINE_CPLUSPLUS

/* The normal alignment of 'long', in bytes. */
#undef ALIGNOF_LONG

/* The normal alignment of 'max_align_t', in bytes. */
#undef ALIGNOF_MAX_ALIGN_T

/* The normal alignment of 'size_t', in bytes. */
#undef ALIGNOF_SIZE_T

/* Alternative SOABI used in debug build to load C extensions built in release
   mode */
#undef ALT_SOABI

/* The Android API level. */
#undef ANDROID_API_LEVEL

/* Define if C doubles are 64-bit IEEE 754 binary format, stored in ARM
   mixed-endian order (byte order 45670123) */
#undef DOUBLE_IS_ARM_MIXED_ENDIAN_IEEE754

/* Define if C doubles are 64-bit IEEE 754 binary format, stored with the most
   significant byte first */
#undef DOUBLE_IS_BIG_ENDIAN_IEEE754

/* Define if C doubles are 64-bit IEEE 754 binary format, stored with the
   least significant byte first */
#undef DOUBLE_IS_LITTLE_ENDIAN_IEEE754

/* Define if --enable-ipv6 is specified */
#undef ENABLE_IPV6

/* Define if getpgrp() must be called as getpgrp(0). */
#undef GETPGRP_HAVE_ARG

/* HACL* library can compile SIMD128 implementations */
#undef HACL_CAN_COMPILE_SIMD128

/* HACL* library can compile SIMD256 implementations */
#undef HACL_CAN_COMPILE_SIMD256

/* Define if you have the 'accept' function. */
#undef HAVE_ACCEPT

/* Define to 1 if you have the 'accept4' function. */
#undef HAVE_ACCEPT4

/* Define to 1 if you have the 'acosh' function. */
#undef HAVE_ACOSH

/* struct addrinfo (netdb.h) */
#undef HAVE_ADDRINFO

/* Define to 1 if you have the 'alarm' function. */
#undef HAVE_ALARM

/* Define if aligned memory access is required */
#undef HAVE_ALIGNED_REQUIRED

/* Define to 1 if you have the <alloca.h> header file. */
#undef HAVE_ALLOCA_H

/* Define this if your time.h defines altzone. */
#undef HAVE_ALTZONE

/* Define to 1 if you have the 'asinh' function. */
#undef HAVE_ASINH

/* Define to 1 if you have the <asm/types.h> header file. */
#undef HAVE_ASM_TYPES_H

/* Define to 1 if you have the 'atanh' function. */
#undef HAVE_ATANH

/* Define if you have the 'bind' function. */
#undef HAVE_BIND

/* Define to 1 if you have the 'bind_textdomain_codeset' function. */
#undef HAVE_BIND_TEXTDOMAIN_CODESET

/* Define to 1 if you have the <bluetooth/bluetooth.h> header file. */
#undef HAVE_BLUETOOTH_BLUETOOTH_H

/* Define to 1 if you have the <bluetooth.h> header file. */
#undef HAVE_BLUETOOTH_H

/* Define if mbstowcs(NULL, "text", 0) does not return the number of wide
   chars that would be converted. */
#undef HAVE_BROKEN_MBSTOWCS

/* Define if nice() returns success/failure instead of the new priority. */
#undef HAVE_BROKEN_NICE

/* Define if the system reports an invalid PIPE_BUF value. */
#undef HAVE_BROKEN_PIPE_BUF

/* Define if poll() sets errno on invalid file descriptors. */
#undef HAVE_BROKEN_POLL

/* Define if the Posix semaphores do not work on your system */
#undef HAVE_BROKEN_POSIX_SEMAPHORES

/* Define if pthread_sigmask() does not work on your system. */
#undef HAVE_BROKEN_PTHREAD_SIGMASK

/* define to 1 if your sem_getvalue is broken. */
#undef HAVE_BROKEN_SEM_GETVALUE

/* Define if 'unsetenv' does not return an int. */
#undef HAVE_BROKEN_UNSETENV

/* Has builtin __atomic_load_n() and __atomic_store_n() functions */
#undef HAVE_BUILTIN_ATOMIC

/* Define to 1 if you have the <bzlib.h> header file. */
#undef HAVE_BZLIB_H

/* Define to 1 if you have the 'chflags' function. */
#undef HAVE_CHFLAGS

/* Define to 1 if you have the 'chmod' function. */
#undef HAVE_CHMOD

/* Define to 1 if you have the 'chown' function. */
#undef HAVE_CHOWN

/* Define if you have the 'chroot' function. */
#undef HAVE_CHROOT

/* Define to 1 if you have the 'clock' function. */
#undef HAVE_CLOCK

/* Define to 1 if you have the 'clock_getres' function. */
#undef HAVE_CLOCK_GETRES

/* Define to 1 if you have the 'clock_gettime' function. */
#undef HAVE_CLOCK_GETTIME

/* Define to 1 if you have the 'clock_nanosleep' function. */
#undef HAVE_CLOCK_NANOSLEEP

/* Define to 1 if you have the 'clock_settime' function. */
#undef HAVE_CLOCK_SETTIME

/* Define to 1 if the system has the type 'clock_t'. */
#undef HAVE_CLOCK_T

/* Define to 1 if you have the 'closefrom' function. */
#undef HAVE_CLOSEFROM

/* Define to 1 if you have the 'close_range' function. */
#undef HAVE_CLOSE_RANGE

/* Define if the C compiler supports computed gotos. */
#undef HAVE_COMPUTED_GOTOS

/* Define to 1 if you have the 'confstr' function. */
#undef HAVE_CONFSTR

/* Define to 1 if you have the <conio.h> header file. */
#undef HAVE_CONIO_H

/* Define if you have the 'connect' function. */
#undef HAVE_CONNECT

/* Define to 1 if you have the 'copy_file_range' function. */
#undef HAVE_COPY_FILE_RANGE

/* Define to 1 if you have the 'ctermid' function. */
#undef HAVE_CTERMID

/* Define if you have the 'ctermid_r' function. */
#undef HAVE_CTERMID_R

/* Define if you have the 'filter' function. */
#undef HAVE_CURSES_FILTER

/* Define to 1 if you have the <curses.h> header file. */
#undef HAVE_CURSES_H

/* Define if you have the 'has_key' function. */
#undef HAVE_CURSES_HAS_KEY

/* Define if you have the 'immedok' function. */
#undef HAVE_CURSES_IMMEDOK

/* Define if you have the 'is_pad' function. */
#undef HAVE_CURSES_IS_PAD

/* Define if you have the 'is_term_resized' function. */
#undef HAVE_CURSES_IS_TERM_RESIZED

/* Define if you have the 'resizeterm' function. */
#undef HAVE_CURSES_RESIZETERM

/* Define if you have the 'resize_term' function. */
#undef HAVE_CURSES_RESIZE_TERM

/* Define if you have the 'syncok' function. */
#undef HAVE_CURSES_SYNCOK

/* Define if you have the 'typeahead' function. */
#undef HAVE_CURSES_TYPEAHEAD

/* Define if you have the 'use_env' function. */
#undef HAVE_CURSES_USE_ENV

/* Define if you have the 'wchgat' function. */
#undef HAVE_CURSES_WCHGAT

/* Define to 1 if you have the <db.h> header file. */
#undef HAVE_DB_H

/* Define to 1 if you have the declaration of 'RTLD_DEEPBIND', and to 0 if you
   don't. */
#undef HAVE_DECL_RTLD_DEEPBIND

/* Define to 1 if you have the declaration of 'RTLD_GLOBAL', and to 0 if you
   don't. */
#undef HAVE_DECL_RTLD_GLOBAL

/* Define to 1 if you have the declaration of 'RTLD_LAZY', and to 0 if you
   don't. */
#undef HAVE_DECL_RTLD_LAZY

/* Define to 1 if you have the declaration of 'RTLD_LOCAL', and to 0 if you
   don't. */
#undef HAVE_DECL_RTLD_LOCAL

/* Define to 1 if you have the declaration of 'RTLD_MEMBER', and to 0 if you
   don't. */
#undef HAVE_DECL_RTLD_MEMBER

/* Define to 1 if you have the declaration of 'RTLD_NODELETE', and to 0 if you
   don't. */
#undef HAVE_DECL_RTLD_NODELETE

/* Define to 1 if you have the declaration of 'RTLD_NOLOAD', and to 0 if you
   don't. */
#undef HAVE_DECL_RTLD_NOLOAD

/* Define to 1 if you have the declaration of 'RTLD_NOW', and to 0 if you
   don't. */
#undef HAVE_DECL_RTLD_NOW

/* Define to 1 if you have the declaration of 'tzname', and to 0 if you don't.
   */
#undef HAVE_DECL_TZNAME

/* Define to 1 if you have the device macros. */
#undef HAVE_DEVICE_MACROS

/* Define to 1 if you have the /dev/ptc device file. */
#undef HAVE_DEV_PTC

/* Define to 1 if you have the /dev/ptmx device file. */
#undef HAVE_DEV_PTMX

/* Define to 1 if you have the <direct.h> header file. */
#undef HAVE_DIRECT_H

/* Define to 1 if the dirent structure has a d_type field */
#undef HAVE_DIRENT_D_TYPE

/* Define to 1 if you have the <dirent.h> header file, and it defines 'DIR'.
   */
#undef HAVE_DIRENT_H

/* Define if you have the 'dirfd' function or macro. */
#undef HAVE_DIRFD

/* Define to 1 if you have the <dlfcn.h> header file. */
#undef HAVE_DLFCN_H

/* Define to 1 if you have the 'dlopen' function. */
#undef HAVE_DLOPEN

/* Define to 1 if you have the 'dup' function. */
#undef HAVE_DUP

/* Define to 1 if you have the 'dup2' function. */
#undef HAVE_DUP2

/* Define to 1 if you have the 'dup3' function. */
#undef HAVE_DUP3

/* Define if you have the '_dyld_shared_cache_contains_path' function. */
#undef HAVE_DYLD_SHARED_CACHE_CONTAINS_PATH

/* Defined when any dynamic module loading is enabled. */
#undef HAVE_DYNAMIC_LOADING

/* Define to 1 if you have the <editline/readline.h> header file. */
#undef HAVE_EDITLINE_READLINE_H

/* Define to 1 if you have the <endian.h> header file. */
#undef HAVE_ENDIAN_H

/* Define if you have the 'epoll_create' function. */
#undef HAVE_EPOLL

/* Define if you have the 'epoll_create1' function. */
#undef HAVE_EPOLL_CREATE1

/* Define to 1 if you have the 'erf' function. */
#undef HAVE_ERF

/* Define to 1 if you have the 'erfc' function. */
#undef HAVE_ERFC

/* Define to 1 if you have the <errno.h> header file. */
#undef HAVE_ERRNO_H

/* Define if you have the 'eventfd' function. */
#undef HAVE_EVENTFD

/* Define to 1 if you have the 'execv' function. */
#undef HAVE_EXECV

/* Define to 1 if you have the 'explicit_bzero' function. */
#undef HAVE_EXPLICIT_BZERO

/* Define to 1 if you have the 'explicit_memset' function. */
#undef HAVE_EXPLICIT_MEMSET

/* Define to 1 if you have the 'expm1' function. */
#undef HAVE_EXPM1

/* Define to 1 if you have the 'faccessat' function. */
#undef HAVE_FACCESSAT

/* Define if you have the 'fchdir' function. */
#undef HAVE_FCHDIR

/* Define to 1 if you have the 'fchmod' function. */
#undef HAVE_FCHMOD

/* Define to 1 if you have the 'fchmodat' function. */
#undef HAVE_FCHMODAT

/* Define to 1 if you have the 'fchown' function. */
#undef HAVE_FCHOWN

/* Define to 1 if you have the 'fchownat' function. */
#undef HAVE_FCHOWNAT

/* Define to 1 if you have the <fcntl.h> header file. */
#undef HAVE_FCNTL_H

/* Define if you have the 'fdatasync' function. */
#undef HAVE_FDATASYNC

/* Define to 1 if you have the 'fdopendir' function. */
#undef HAVE_FDOPENDIR

/* Define to 1 if you have the 'fdwalk' function. */
#undef HAVE_FDWALK

/* Define to 1 if you have the 'fexecve' function. */
#undef HAVE_FEXECVE

/* Define if you have the 'ffi_closure_alloc' function. */
#undef HAVE_FFI_CLOSURE_ALLOC

/* Define if you have the 'ffi_prep_cif_var' function. */
#undef HAVE_FFI_PREP_CIF_VAR

/* Define if you have the 'ffi_prep_closure_loc' function. */
#undef HAVE_FFI_PREP_CLOSURE_LOC

/* Define to 1 if you have the 'flock' function. */
#undef HAVE_FLOCK

/* Define to 1 if you have the 'fork' function. */
#undef HAVE_FORK

/* Define to 1 if you have the 'fork1' function. */
#undef HAVE_FORK1

/* Define to 1 if you have the 'forkpty' function. */
#undef HAVE_FORKPTY

/* Define to 1 if you have the 'fpathconf' function. */
#undef HAVE_FPATHCONF

/* Define to 1 if you have the 'fseek64' function. */
#undef HAVE_FSEEK64

/* Define to 1 if you have the 'fseeko' function. */
#undef HAVE_FSEEKO

/* Define to 1 if you have the 'fstatat' function. */
#undef HAVE_FSTATAT

/* Define to 1 if you have the 'fstatvfs' function. */
#undef HAVE_FSTATVFS

/* Define if you have the 'fsync' function. */
#undef HAVE_FSYNC

/* Define to 1 if you have the 'ftell64' function. */
#undef HAVE_FTELL64

/* Define to 1 if you have the 'ftello' function. */
#undef HAVE_FTELLO

/* Define to 1 if you have the 'ftime' function. */
#undef HAVE_FTIME

/* Define to 1 if you have the 'ftruncate' function. */
#undef HAVE_FTRUNCATE

/* Define to 1 if you have the 'futimens' function. */
#undef HAVE_FUTIMENS

/* Define to 1 if you have the 'futimes' function. */
#undef HAVE_FUTIMES

/* Define to 1 if you have the 'futimesat' function. */
#undef HAVE_FUTIMESAT

/* Define to 1 if you have the 'gai_strerror' function. */
#undef HAVE_GAI_STRERROR

/* Define if we can use gcc inline assembler to get and set mc68881 fpcr */
#undef HAVE_GCC_ASM_FOR_MC68881

/* Define if we can use x64 gcc inline assembler */
#undef HAVE_GCC_ASM_FOR_X64

/* Define if we can use gcc inline assembler to get and set x87 control word
   */
#undef HAVE_GCC_ASM_FOR_X87

/* Define if your compiler provides __uint128_t */
#undef HAVE_GCC_UINT128_T

/* Define to 1 if you have the <gdbm-ndbm.h> header file. */
#undef HAVE_GDBM_DASH_NDBM_H

/* Define to 1 if you have the <gdbm.h> header file. */
#undef HAVE_GDBM_H

/* Define to 1 if you have the <gdbm/ndbm.h> header file. */
#undef HAVE_GDBM_NDBM_H

/* Define if you have the getaddrinfo function. */
#undef HAVE_GETADDRINFO

/* Define this if you have flockfile(), getc_unlocked(), and funlockfile() */
#undef HAVE_GETC_UNLOCKED

/* Define to 1 if you have the 'getegid' function. */
#undef HAVE_GETEGID

/* Define to 1 if you have the 'getentropy' function. */
#undef HAVE_GETENTROPY

/* Define to 1 if you have the 'geteuid' function. */
#undef HAVE_GETEUID

/* Define to 1 if you have the 'getgid' function. */
#undef HAVE_GETGID

/* Define to 1 if you have the 'getgrent' function. */
#undef HAVE_GETGRENT

/* Define to 1 if you have the 'getgrgid' function. */
#undef HAVE_GETGRGID

/* Define to 1 if you have the 'getgrgid_r' function. */
#undef HAVE_GETGRGID_R

/* Define to 1 if you have the 'getgrnam_r' function. */
#undef HAVE_GETGRNAM_R

/* Define to 1 if you have the 'getgrouplist' function. */
#undef HAVE_GETGROUPLIST

/* Define to 1 if you have the 'getgroups' function. */
#undef HAVE_GETGROUPS

/* Define if you have the 'gethostbyaddr' function. */
#undef HAVE_GETHOSTBYADDR

/* Define to 1 if you have the 'gethostbyname' function. */
#undef HAVE_GETHOSTBYNAME

/* Define this if you have some version of gethostbyname_r() */
#undef HAVE_GETHOSTBYNAME_R

/* Define this if you have the 3-arg version of gethostbyname_r(). */
#undef HAVE_GETHOSTBYNAME_R_3_ARG

/* Define this if you have the 5-arg version of gethostbyname_r(). */
#undef HAVE_GETHOSTBYNAME_R_5_ARG

/* Define this if you have the 6-arg version of gethostbyname_r(). */
#undef HAVE_GETHOSTBYNAME_R_6_ARG

/* Define to 1 if you have the 'gethostname' function. */
#undef HAVE_GETHOSTNAME

/* Define to 1 if you have the 'getitimer' function. */
#undef HAVE_GETITIMER

/* Define to 1 if you have the 'getloadavg' function. */
#undef HAVE_GETLOADAVG

/* Define to 1 if you have the 'getlogin' function. */
#undef HAVE_GETLOGIN

/* Define to 1 if you have the 'getnameinfo' function. */
#undef HAVE_GETNAMEINFO

/* Define if you have the 'getpagesize' function. */
#undef HAVE_GETPAGESIZE

/* Define if you have the 'getpeername' function. */
#undef HAVE_GETPEERNAME

/* Define to 1 if you have the 'getpgid' function. */
#undef HAVE_GETPGID

/* Define to 1 if you have the 'getpgrp' function. */
#undef HAVE_GETPGRP

/* Define to 1 if you have the 'getpid' function. */
#undef HAVE_GETPID

/* Define to 1 if you have the 'getppid' function. */
#undef HAVE_GETPPID

/* Define to 1 if you have the 'getpriority' function. */
#undef HAVE_GETPRIORITY

/* Define if you have the 'getprotobyname' function. */
#undef HAVE_GETPROTOBYNAME

/* Define to 1 if you have the 'getpwent' function. */
#undef HAVE_GETPWENT

/* Define to 1 if you have the 'getpwnam_r' function. */
#undef HAVE_GETPWNAM_R

/* Define to 1 if you have the 'getpwuid' function. */
#undef HAVE_GETPWUID

/* Define to 1 if you have the 'getpwuid_r' function. */
#undef HAVE_GETPWUID_R

/* Define to 1 if the getrandom() function is available */
#undef HAVE_GETRANDOM

/* Define to 1 if the Linux getrandom() syscall is available */
#undef HAVE_GETRANDOM_SYSCALL

/* Define to 1 if you have the 'getresgid' function. */
#undef HAVE_GETRESGID

/* Define to 1 if you have the 'getresuid' function. */
#undef HAVE_GETRESUID

/* Define to 1 if you have the 'getrusage' function. */
#undef HAVE_GETRUSAGE

/* Define if you have the 'getservbyname' function. */
#undef HAVE_GETSERVBYNAME

/* Define if you have the 'getservbyport' function. */
#undef HAVE_GETSERVBYPORT

/* Define to 1 if you have the 'getsid' function. */
#undef HAVE_GETSID

/* Define if you have the 'getsockname' function. */
#undef HAVE_GETSOCKNAME

/* Define to 1 if you have the 'getspent' function. */
#undef HAVE_GETSPENT

/* Define to 1 if you have the 'getspnam' function. */
#undef HAVE_GETSPNAM

/* Define to 1 if you have the 'getuid' function. */
#undef HAVE_GETUID

/* Define to 1 if you have the 'getwd' function. */
#undef HAVE_GETWD

/* Define if glibc has incorrect _FORTIFY_SOURCE wrappers for memmove and
   bcopy. */
#undef HAVE_GLIBC_MEMMOVE_BUG

/* Define to 1 if you have the 'grantpt' function. */
#undef HAVE_GRANTPT

/* Define to 1 if you have the <grp.h> header file. */
#undef HAVE_GRP_H

/* Define if you have the 'hstrerror' function. */
#undef HAVE_HSTRERROR

/* Define this if you have le64toh() */
#undef HAVE_HTOLE64

/* Define to 1 if you have the 'if_nameindex' function. */
#undef HAVE_IF_NAMEINDEX

/* Define if you have the 'inet_aton' function. */
#undef HAVE_INET_ATON

/* Define if you have the 'inet_ntoa' function. */
#undef HAVE_INET_NTOA

/* Define if you have the 'inet_pton' function. */
#undef HAVE_INET_PTON

/* Define to 1 if you have the 'initgroups' function. */
#undef HAVE_INITGROUPS

/* Define to 1 if you have the <inttypes.h> header file. */
#undef HAVE_INTTYPES_H

/* Define to 1 if you have the <io.h> header file. */
#undef HAVE_IO_H

/* Define if gcc has the ipa-pure-const bug. */
#undef HAVE_IPA_PURE_CONST_BUG

/* Define to 1 if you have the 'kill' function. */
#undef HAVE_KILL

/* Define to 1 if you have the 'killpg' function. */
#undef HAVE_KILLPG

/* Define if you have the 'kqueue' function. */
#undef HAVE_KQUEUE

/* Define to 1 if you have the <langinfo.h> header file. */
#undef HAVE_LANGINFO_H

/* Defined to enable large file support when an off_t is bigger than a long
   and long long is at least as big as an off_t. You may need to add some
   flags for configuration and compilation to enable this mode. (For Solaris
   and Linux, the necessary defines are already defined.) */
#undef HAVE_LARGEFILE_SUPPORT

/* Define to 1 if you have the 'lchflags' function. */
#undef HAVE_LCHFLAGS

/* Define to 1 if you have the 'lchmod' function. */
#undef HAVE_LCHMOD

/* Define to 1 if you have the 'lchown' function. */
#undef HAVE_LCHOWN

/* Define to 1 if you have the `db' library (-ldb). */
#undef HAVE_LIBDB

/* Define to 1 if you have the 'dl' library (-ldl). */
#undef HAVE_LIBDL

/* Define to 1 if you have the 'dld' library (-ldld). */
#undef HAVE_LIBDLD

/* Define to 1 if you have the 'ieee' library (-lieee). */
#undef HAVE_LIBIEEE

/* Define to 1 if you have the <libintl.h> header file. */
#undef HAVE_LIBINTL_H

/* Define to 1 if you have the 'sendfile' library (-lsendfile). */
#undef HAVE_LIBSENDFILE

/* Define to 1 if you have the 'sqlite3' library (-lsqlite3). */
#undef HAVE_LIBSQLITE3

/* Define to 1 if you have the <libutil.h> header file. */
#undef HAVE_LIBUTIL_H

/* Define if you have the 'link' function. */
#undef HAVE_LINK

/* Define to 1 if you have the 'linkat' function. */
#undef HAVE_LINKAT

/* Define to 1 if you have the <linux/auxvec.h> header file. */
#undef HAVE_LINUX_AUXVEC_H

/* Define to 1 if you have the <linux/can/bcm.h> header file. */
#undef HAVE_LINUX_CAN_BCM_H

/* Define to 1 if you have the <linux/can.h> header file. */
#undef HAVE_LINUX_CAN_H

/* Define to 1 if you have the <linux/can/j1939.h> header file. */
#undef HAVE_LINUX_CAN_J1939_H

/* Define if compiling using Linux 3.6 or later. */
#undef HAVE_LINUX_CAN_RAW_FD_FRAMES

/* Define to 1 if you have the <linux/can/raw.h> header file. */
#undef HAVE_LINUX_CAN_RAW_H

/* Define if compiling using Linux 4.1 or later. */
#undef HAVE_LINUX_CAN_RAW_JOIN_FILTERS

/* Define to 1 if you have the <linux/fs.h> header file. */
#undef HAVE_LINUX_FS_H

/* Define to 1 if you have the <linux/limits.h> header file. */
#undef HAVE_LINUX_LIMITS_H

/* Define to 1 if you have the <linux/memfd.h> header file. */
#undef HAVE_LINUX_MEMFD_H

/* Define to 1 if you have the <linux/netfilter_ipv4.h> header file. */
#undef HAVE_LINUX_NETFILTER_IPV4_H

/* Define to 1 if you have the <linux/netlink.h> header file. */
#undef HAVE_LINUX_NETLINK_H

/* Define to 1 if you have the <linux/qrtr.h> header file. */
#undef HAVE_LINUX_QRTR_H

/* Define to 1 if you have the <linux/random.h> header file. */
#undef HAVE_LINUX_RANDOM_H

/* Define to 1 if you have the <linux/sched.h> header file. */
#undef HAVE_LINUX_SCHED_H

/* Define to 1 if you have the <linux/soundcard.h> header file. */
#undef HAVE_LINUX_SOUNDCARD_H

/* Define to 1 if you have the <linux/tipc.h> header file. */
#undef HAVE_LINUX_TIPC_H

/* Define to 1 if you have the <linux/vm_sockets.h> header file. */
#undef HAVE_LINUX_VM_SOCKETS_H

/* Define to 1 if you have the <linux/wait.h> header file. */
#undef HAVE_LINUX_WAIT_H

/* Define if you have the 'listen' function. */
#undef HAVE_LISTEN

/* Define to 1 if you have the 'lockf' function. */
#undef HAVE_LOCKF

/* Define to 1 if you have the 'log1p' function. */
#undef HAVE_LOG1P

/* Define to 1 if you have the 'log2' function. */
#undef HAVE_LOG2

/* Define to 1 if you have the `login_tty' function. */
#undef HAVE_LOGIN_TTY

/* Define to 1 if the system has the type 'long double'. */
#undef HAVE_LONG_DOUBLE

/* Define to 1 if you have the 'lstat' function. */
#undef HAVE_LSTAT

/* Define to 1 if you have the 'lutimes' function. */
#undef HAVE_LUTIMES

/* Define to 1 if you have the <lzma.h> header file. */
#undef HAVE_LZMA_H

/* Define to 1 if you have the 'madvise' function. */
#undef HAVE_MADVISE

/* Define this if you have the makedev macro. */
#undef HAVE_MAKEDEV

/* Define to 1 if you have the 'mbrtowc' function. */
#undef HAVE_MBRTOWC

/* Define if you have the 'memfd_create' function. */
#undef HAVE_MEMFD_CREATE

/* Define to 1 if you have the 'memrchr' function. */
#undef HAVE_MEMRCHR

/* Define to 1 if you have the <minix/config.h> header file. */
#undef HAVE_MINIX_CONFIG_H

/* Define to 1 if you have the 'mkdirat' function. */
#undef HAVE_MKDIRAT

/* Define to 1 if you have the 'mkfifo' function. */
#undef HAVE_MKFIFO

/* Define to 1 if you have the 'mkfifoat' function. */
#undef HAVE_MKFIFOAT

/* Define to 1 if you have the 'mknod' function. */
#undef HAVE_MKNOD

/* Define to 1 if you have the 'mknodat' function. */
#undef HAVE_MKNODAT

/* Define to 1 if you have the 'mktime' function. */
#undef HAVE_MKTIME

/* Define to 1 if you have the 'mmap' function. */
#undef HAVE_MMAP

/* Define to 1 if you have the 'mremap' function. */
#undef HAVE_MREMAP

/* Define to 1 if you have the 'nanosleep' function. */
#undef HAVE_NANOSLEEP

/* Define if you have the 'ncurses' library */
#undef HAVE_NCURSES

/* Define if you have the 'ncursesw' library */
#undef HAVE_NCURSESW

/* Define to 1 if you have the <ncursesw/curses.h> header file. */
#undef HAVE_NCURSESW_CURSES_H

/* Define to 1 if you have the <ncursesw/ncurses.h> header file. */
#undef HAVE_NCURSESW_NCURSES_H

/* Define to 1 if you have the <ncursesw/panel.h> header file. */
#undef HAVE_NCURSESW_PANEL_H

/* Define to 1 if you have the <ncurses/curses.h> header file. */
#undef HAVE_NCURSES_CURSES_H

/* Define to 1 if you have the <ncurses.h> header file. */
#undef HAVE_NCURSES_H

/* Define to 1 if you have the <ncurses/ncurses.h> header file. */
#undef HAVE_NCURSES_NCURSES_H

/* Define to 1 if you have the <ncurses/panel.h> header file. */
#undef HAVE_NCURSES_PANEL_H

/* Define to 1 if you have the <ndbm.h> header file. */
#undef HAVE_NDBM_H

/* Define to 1 if you have the <ndir.h> header file, and it defines 'DIR'. */
#undef HAVE_NDIR_H

/* Define to 1 if you have the <netcan/can.h> header file. */
#undef HAVE_NETCAN_CAN_H

/* Define to 1 if you have the <netdb.h> header file. */
#undef HAVE_NETDB_H

/* Define to 1 if you have the <netinet/in.h> header file. */
#undef HAVE_NETINET_IN_H

/* Define to 1 if you have the <netlink/netlink.h> header file. */
#undef HAVE_NETLINK_NETLINK_H

/* Define to 1 if you have the <netpacket/packet.h> header file. */
#undef HAVE_NETPACKET_PACKET_H

/* Define to 1 if you have the <net/ethernet.h> header file. */
#undef HAVE_NET_ETHERNET_H

/* Define to 1 if you have the <net/if.h> header file. */
#undef HAVE_NET_IF_H

/* Define to 1 if you have the 'nice' function. */
#undef HAVE_NICE

/* Define if the internal form of wchar_t in non-Unicode locales is not
   Unicode. */
#undef HAVE_NON_UNICODE_WCHAR_T_REPRESENTATION

/* Define to 1 if you have the 'openat' function. */
#undef HAVE_OPENAT

/* Define to 1 if you have the 'opendir' function. */
#undef HAVE_OPENDIR

/* Define to 1 if you have the 'openpty' function. */
#undef HAVE_OPENPTY

/* Define if you have the 'panel' library */
#undef HAVE_PANEL

/* Define if you have the 'panelw' library */
#undef HAVE_PANELW

/* Define to 1 if you have the <panel.h> header file. */
#undef HAVE_PANEL_H

/* Define to 1 if you have the 'pathconf' function. */
#undef HAVE_PATHCONF

/* Define to 1 if you have the 'pause' function. */
#undef HAVE_PAUSE

/* Define to 1 if you have the 'pipe' function. */
#undef HAVE_PIPE

/* Define to 1 if you have the 'pipe2' function. */
#undef HAVE_PIPE2

/* Define to 1 if you have the 'plock' function. */
#undef HAVE_PLOCK

/* Define to 1 if you have the 'poll' function. */
#undef HAVE_POLL

/* Define to 1 if you have the <poll.h> header file. */
#undef HAVE_POLL_H

/* Define to 1 if you have the 'posix_fadvise' function. */
#undef HAVE_POSIX_FADVISE

/* Define to 1 if you have the 'posix_fallocate' function. */
#undef HAVE_POSIX_FALLOCATE

/* Define to 1 if you have the 'posix_openpt' function. */
#undef HAVE_POSIX_OPENPT

/* Define to 1 if you have the 'posix_spawn' function. */
#undef HAVE_POSIX_SPAWN

/* Define to 1 if you have the 'posix_spawnp' function. */
#undef HAVE_POSIX_SPAWNP

/* Define to 1 if you have the 'posix_spawn_file_actions_addclosefrom_np'
   function. */
#undef HAVE_POSIX_SPAWN_FILE_ACTIONS_ADDCLOSEFROM_NP

/* Define to 1 if you have the 'pread' function. */
#undef HAVE_PREAD

/* Define to 1 if you have the 'preadv' function. */
#undef HAVE_PREADV

/* Define to 1 if you have the 'preadv2' function. */
#undef HAVE_PREADV2

/* Define if you have the 'prlimit' function. */
#undef HAVE_PRLIMIT

/* Define to 1 if you have the <process.h> header file. */
#undef HAVE_PROCESS_H

/* Define to 1 if you have the 'process_vm_readv' function. */
#undef HAVE_PROCESS_VM_READV

/* Define if your compiler supports function prototype */
#undef HAVE_PROTOTYPES

/* Define to 1 if you have the 'pthread_condattr_setclock' function. */
#undef HAVE_PTHREAD_CONDATTR_SETCLOCK

/* Define to 1 if you have the 'pthread_cond_timedwait_relative_np' function.
   */
#undef HAVE_PTHREAD_COND_TIMEDWAIT_RELATIVE_NP

/* Defined for Solaris 2.6 bug in pthread header. */
#undef HAVE_PTHREAD_DESTRUCTOR

/* Define to 1 if you have the 'pthread_getcpuclockid' function. */
#undef HAVE_PTHREAD_GETCPUCLOCKID

/* Define to 1 if you have the 'pthread_getname_np' function. */
#undef HAVE_PTHREAD_GETNAME_NP

/* Define to 1 if you have the <pthread.h> header file. */
#undef HAVE_PTHREAD_H

/* Define to 1 if you have the 'pthread_init' function. */
#undef HAVE_PTHREAD_INIT

/* Define to 1 if you have the 'pthread_kill' function. */
#undef HAVE_PTHREAD_KILL

/* Define to 1 if you have the 'pthread_setname_np' function. */
#undef HAVE_PTHREAD_SETNAME_NP

/* Define to 1 if you have the 'pthread_sigmask' function. */
#undef HAVE_PTHREAD_SIGMASK

/* Define if platform requires stubbed pthreads support */
#undef HAVE_PTHREAD_STUBS

/* Define to 1 if you have the 'ptsname' function. */
#undef HAVE_PTSNAME

/* Define to 1 if you have the 'ptsname_r' function. */
#undef HAVE_PTSNAME_R

/* Define to 1 if you have the <pty.h> header file. */
#undef HAVE_PTY_H

/* Define to 1 if you have the 'pwrite' function. */
#undef HAVE_PWRITE

/* Define to 1 if you have the 'pwritev' function. */
#undef HAVE_PWRITEV

/* Define to 1 if you have the 'pwritev2' function. */
#undef HAVE_PWRITEV2

/* Define to 1 if you have the <readline/readline.h> header file. */
#undef HAVE_READLINE_READLINE_H

/* Define to 1 if you have the 'readlink' function. */
#undef HAVE_READLINK

/* Define to 1 if you have the 'readlinkat' function. */
#undef HAVE_READLINKAT

/* Define to 1 if you have the 'readv' function. */
#undef HAVE_READV

/* Define to 1 if you have the 'realpath' function. */
#undef HAVE_REALPATH

/* Define if you have the 'recvfrom' function. */
#undef HAVE_RECVFROM

/* Define to 1 if you have the 'renameat' function. */
#undef HAVE_RENAMEAT

/* Define if readline supports append_history */
#undef HAVE_RL_APPEND_HISTORY

/* Define if you can turn off readline's signal handling. */
#undef HAVE_RL_CATCH_SIGNAL

/* Define to 1 if the system has the type 'rl_compdisp_func_t'. */
#undef HAVE_RL_COMPDISP_FUNC_T

/* Define if you have readline 2.2 */
#undef HAVE_RL_COMPLETION_APPEND_CHARACTER

/* Define if you have readline 4.0 */
#undef HAVE_RL_COMPLETION_DISPLAY_MATCHES_HOOK

/* Define if you have readline 4.2 */
#undef HAVE_RL_COMPLETION_MATCHES

/* Define if you have rl_completion_suppress_append */
#undef HAVE_RL_COMPLETION_SUPPRESS_APPEND

/* Define if you have readline 4.0 */
#undef HAVE_RL_PRE_INPUT_HOOK

/* Define if you have readline 4.0 */
#undef HAVE_RL_RESIZE_TERMINAL

/* Define to 1 if you have the 'rtpSpawn' function. */
#undef HAVE_RTPSPAWN

/* Define to 1 if you have the 'sched_get_priority_max' function. */
#undef HAVE_SCHED_GET_PRIORITY_MAX

/* Define to 1 if you have the <sched.h> header file. */
#undef HAVE_SCHED_H

/* Define to 1 if you have the 'sched_rr_get_interval' function. */
#undef HAVE_SCHED_RR_GET_INTERVAL

/* Define to 1 if you have the 'sched_setaffinity' function. */
#undef HAVE_SCHED_SETAFFINITY

/* Define to 1 if you have the 'sched_setparam' function. */
#undef HAVE_SCHED_SETPARAM

/* Define to 1 if you have the 'sched_setscheduler' function. */
#undef HAVE_SCHED_SETSCHEDULER

/* Define to 1 if you have the 'sem_clockwait' function. */
#undef HAVE_SEM_CLOCKWAIT

/* Define to 1 if you have the 'sem_getvalue' function. */
#undef HAVE_SEM_GETVALUE

/* Define to 1 if you have the 'sem_open' function. */
#undef HAVE_SEM_OPEN

/* Define to 1 if you have the 'sem_timedwait' function. */
#undef HAVE_SEM_TIMEDWAIT

/* Define to 1 if you have the 'sem_unlink' function. */
#undef HAVE_SEM_UNLINK

/* Define to 1 if you have the 'sendfile' function. */
#undef HAVE_SENDFILE

/* Define if you have the 'sendto' function. */
#undef HAVE_SENDTO

/* Define to 1 if you have the 'setegid' function. */
#undef HAVE_SETEGID

/* Define to 1 if you have the 'seteuid' function. */
#undef HAVE_SETEUID

/* Define to 1 if you have the 'setgid' function. */
#undef HAVE_SETGID

/* Define if you have the 'setgroups' function. */
#undef HAVE_SETGROUPS

/* Define to 1 if you have the 'sethostname' function. */
#undef HAVE_SETHOSTNAME

/* Define to 1 if you have the 'setitimer' function. */
#undef HAVE_SETITIMER

/* Define to 1 if you have the <setjmp.h> header file. */
#undef HAVE_SETJMP_H

/* Define to 1 if you have the 'setlocale' function. */
#undef HAVE_SETLOCALE

/* Define to 1 if you have the 'setns' function. */
#undef HAVE_SETNS

/* Define to 1 if you have the 'setpgid' function. */
#undef HAVE_SETPGID

/* Define to 1 if you have the 'setpgrp' function. */
#undef HAVE_SETPGRP

/* Define to 1 if you have the 'setpriority' function. */
#undef HAVE_SETPRIORITY

/* Define to 1 if you have the 'setregid' function. */
#undef HAVE_SETREGID

/* Define to 1 if you have the 'setresgid' function. */
#undef HAVE_SETRESGID

/* Define to 1 if you have the 'setresuid' function. */
#undef HAVE_SETRESUID

/* Define to 1 if you have the 'setreuid' function. */
#undef HAVE_SETREUID

/* Define to 1 if you have the 'setsid' function. */
#undef HAVE_SETSID

/* Define if you have the 'setsockopt' function. */
#undef HAVE_SETSOCKOPT

/* Define to 1 if you have the 'setuid' function. */
#undef HAVE_SETUID

/* Define to 1 if you have the 'setvbuf' function. */
#undef HAVE_SETVBUF

/* Define to 1 if you have the <shadow.h> header file. */
#undef HAVE_SHADOW_H

/* Define to 1 if you have the 'shm_open' function. */
#undef HAVE_SHM_OPEN

/* Define to 1 if you have the 'shm_unlink' function. */
#undef HAVE_SHM_UNLINK

/* Define to 1 if you have the 'shutdown' function. */
#undef HAVE_SHUTDOWN

/* Define to 1 if you have the 'sigaction' function. */
#undef HAVE_SIGACTION

/* Define to 1 if you have the 'sigaltstack' function. */
#undef HAVE_SIGALTSTACK

/* Define to 1 if you have the 'sigfillset' function. */
#undef HAVE_SIGFILLSET

/* Define to 1 if 'si_band' is a member of 'siginfo_t'. */
#undef HAVE_SIGINFO_T_SI_BAND

/* Define to 1 if you have the 'siginterrupt' function. */
#undef HAVE_SIGINTERRUPT

/* Define to 1 if you have the <signal.h> header file. */
#undef HAVE_SIGNAL_H

/* Define to 1 if you have the 'sigpending' function. */
#undef HAVE_SIGPENDING

/* Define to 1 if you have the 'sigrelse' function. */
#undef HAVE_SIGRELSE

/* Define to 1 if you have the 'sigtimedwait' function. */
#undef HAVE_SIGTIMEDWAIT

/* Define to 1 if you have the 'sigwait' function. */
#undef HAVE_SIGWAIT

/* Define to 1 if you have the 'sigwaitinfo' function. */
#undef HAVE_SIGWAITINFO

/* Define to 1 if you have the 'snprintf' function. */
#undef HAVE_SNPRINTF

/* struct sockaddr_alg (linux/if_alg.h) */
#undef HAVE_SOCKADDR_ALG

/* Define if sockaddr has sa_len member */
#undef HAVE_SOCKADDR_SA_LEN

/* struct sockaddr_storage (sys/socket.h) */
#undef HAVE_SOCKADDR_STORAGE

/* Define if you have the 'socket' function. */
#undef HAVE_SOCKET

/* Define if you have the 'socketpair' function. */
#undef HAVE_SOCKETPAIR

/* Define to 1 if the system has the type 'socklen_t'. */
#undef HAVE_SOCKLEN_T

/* Define to 1 if you have the <spawn.h> header file. */
#undef HAVE_SPAWN_H

/* Define to 1 if you have the 'splice' function. */
#undef HAVE_SPLICE

/* Define to 1 if the system has the type 'ssize_t'. */
#undef HAVE_SSIZE_T

/* Define to 1 if you have the 'statvfs' function. */
#undef HAVE_STATVFS

/* Define if you have struct stat.st_mtim.tv_nsec */
#undef HAVE_STAT_TV_NSEC

/* Define if you have struct stat.st_mtimensec */
#undef HAVE_STAT_TV_NSEC2

/* Define to 1 if you have the <stdint.h> header file. */
#undef HAVE_STDINT_H

/* Define to 1 if you have the <stdio.h> header file. */
#undef HAVE_STDIO_H

/* Define to 1 if you have the <stdlib.h> header file. */
#undef HAVE_STDLIB_H

/* Has stdatomic.h with atomic_int and atomic_uintptr_t */
#undef HAVE_STD_ATOMIC

/* Define to 1 if you have the 'strftime' function. */
#undef HAVE_STRFTIME

/* Define to 1 if you have the <strings.h> header file. */
#undef HAVE_STRINGS_H

/* Define to 1 if you have the <string.h> header file. */
#undef HAVE_STRING_H

/* Define to 1 if you have the 'strlcpy' function. */
#undef HAVE_STRLCPY

/* Define to 1 if you have the <stropts.h> header file. */
#undef HAVE_STROPTS_H

/* Define to 1 if you have the 'strsignal' function. */
#undef HAVE_STRSIGNAL

/* Define to 1 if 'pw_gecos' is a member of 'struct passwd'. */
#undef HAVE_STRUCT_PASSWD_PW_GECOS

/* Define to 1 if 'pw_passwd' is a member of 'struct passwd'. */
#undef HAVE_STRUCT_PASSWD_PW_PASSWD

/* Define to 1 if 'st_birthtime' is a member of 'struct stat'. */
#undef HAVE_STRUCT_STAT_ST_BIRTHTIME

/* Define to 1 if 'st_blksize' is a member of 'struct stat'. */
#undef HAVE_STRUCT_STAT_ST_BLKSIZE

/* Define to 1 if 'st_blocks' is a member of 'struct stat'. */
#undef HAVE_STRUCT_STAT_ST_BLOCKS

/* Define to 1 if 'st_flags' is a member of 'struct stat'. */
#undef HAVE_STRUCT_STAT_ST_FLAGS

/* Define to 1 if 'st_gen' is a member of 'struct stat'. */
#undef HAVE_STRUCT_STAT_ST_GEN

/* Define to 1 if 'st_rdev' is a member of 'struct stat'. */
#undef HAVE_STRUCT_STAT_ST_RDEV

/* Define to 1 if 'tm_zone' is a member of 'struct tm'. */
#undef HAVE_STRUCT_TM_TM_ZONE

/* Define if you have the 'symlink' function. */
#undef HAVE_SYMLINK

/* Define to 1 if you have the 'symlinkat' function. */
#undef HAVE_SYMLINKAT

/* Define to 1 if you have the 'sync' function. */
#undef HAVE_SYNC

/* Define to 1 if you have the 'sysconf' function. */
#undef HAVE_SYSCONF

/* Define to 1 if you have the <sysexits.h> header file. */
#undef HAVE_SYSEXITS_H

/* Define to 1 if you have the <syslog.h> header file. */
#undef HAVE_SYSLOG_H

/* Define to 1 if you have the 'system' function. */
#undef HAVE_SYSTEM

/* Define to 1 if you have the <sys/audioio.h> header file. */
#undef HAVE_SYS_AUDIOIO_H

/* Define to 1 if you have the <sys/auxv.h> header file. */
#undef HAVE_SYS_AUXV_H

/* Define to 1 if you have the <sys/bsdtty.h> header file. */
#undef HAVE_SYS_BSDTTY_H

/* Define to 1 if you have the <sys/devpoll.h> header file. */
#undef HAVE_SYS_DEVPOLL_H

/* Define to 1 if you have the <sys/dir.h> header file, and it defines 'DIR'.
   */
#undef HAVE_SYS_DIR_H

/* Define to 1 if you have the <sys/endian.h> header file. */
#undef HAVE_SYS_ENDIAN_H

/* Define to 1 if you have the <sys/epoll.h> header file. */
#undef HAVE_SYS_EPOLL_H

/* Define to 1 if you have the <sys/eventfd.h> header file. */
#undef HAVE_SYS_EVENTFD_H

/* Define to 1 if you have the <sys/event.h> header file. */
#undef HAVE_SYS_EVENT_H

/* Define to 1 if you have the <sys/file.h> header file. */
#undef HAVE_SYS_FILE_H

/* Define to 1 if you have the <sys/ioctl.h> header file. */
#undef HAVE_SYS_IOCTL_H

/* Define to 1 if you have the <sys/kern_control.h> header file. */
#undef HAVE_SYS_KERN_CONTROL_H

/* Define to 1 if you have the <sys/loadavg.h> header file. */
#undef HAVE_SYS_LOADAVG_H

/* Define to 1 if you have the <sys/lock.h> header file. */
#undef HAVE_SYS_LOCK_H

/* Define to 1 if you have the <sys/memfd.h> header file. */
#undef HAVE_SYS_MEMFD_H

/* Define to 1 if you have the <sys/mkdev.h> header file. */
#undef HAVE_SYS_MKDEV_H

/* Define to 1 if you have the <sys/mman.h> header file. */
#undef HAVE_SYS_MMAN_H

/* Define to 1 if you have the <sys/modem.h> header file. */
#undef HAVE_SYS_MODEM_H

/* Define to 1 if you have the <sys/ndir.h> header file, and it defines 'DIR'.
   */
#undef HAVE_SYS_NDIR_H

/* Define to 1 if you have the <sys/param.h> header file. */
#undef HAVE_SYS_PARAM_H

/* Define to 1 if you have the <sys/pidfd.h> header file. */
#undef HAVE_SYS_PIDFD_H

/* Define to 1 if you have the <sys/poll.h> header file. */
#undef HAVE_SYS_POLL_H

/* Define to 1 if you have the <sys/random.h> header file. */
#undef HAVE_SYS_RANDOM_H

/* Define to 1 if you have the <sys/resource.h> header file. */
#undef HAVE_SYS_RESOURCE_H

/* Define to 1 if you have the <sys/select.h> header file. */
#undef HAVE_SYS_SELECT_H

/* Define to 1 if you have the <sys/sendfile.h> header file. */
#undef HAVE_SYS_SENDFILE_H

/* Define to 1 if you have the <sys/socket.h> header file. */
#undef HAVE_SYS_SOCKET_H

/* Define to 1 if you have the <sys/soundcard.h> header file. */
#undef HAVE_SYS_SOUNDCARD_H

/* Define to 1 if you have the <sys/statvfs.h> header file. */
#undef HAVE_SYS_STATVFS_H

/* Define to 1 if you have the <sys/stat.h> header file. */
#undef HAVE_SYS_STAT_H

/* Define to 1 if you have the <sys/syscall.h> header file. */
#undef HAVE_SYS_SYSCALL_H

/* Define to 1 if you have the <sys/sysmacros.h> header file. */
#undef HAVE_SYS_SYSMACROS_H

/* Define to 1 if you have the <sys/sys_domain.h> header file. */
#undef HAVE_SYS_SYS_DOMAIN_H

/* Define to 1 if you have the <sys/termio.h> header file. */
#undef HAVE_SYS_TERMIO_H

/* Define to 1 if you have the <sys/timerfd.h> header file. */
#undef HAVE_SYS_TIMERFD_H

/* Define to 1 if you have the <sys/times.h> header file. */
#undef HAVE_SYS_TIMES_H

/* Define to 1 if you have the <sys/time.h> header file. */
#undef HAVE_SYS_TIME_H

/* Define to 1 if you have the <sys/types.h> header file. */
#undef HAVE_SYS_TYPES_H

/* Define to 1 if you have the <sys/uio.h> header file. */
#undef HAVE_SYS_UIO_H

/* Define to 1 if you have the <sys/un.h> header file. */
#undef HAVE_SYS_UN_H

/* Define to 1 if you have the <sys/utsname.h> header file. */
#undef HAVE_SYS_UTSNAME_H

/* Define to 1 if you have the <sys/wait.h> header file. */
#undef HAVE_SYS_WAIT_H

/* Define to 1 if you have the <sys/xattr.h> header file. */
#undef HAVE_SYS_XATTR_H

/* Define to 1 if you have the 'tcgetpgrp' function. */
#undef HAVE_TCGETPGRP

/* Define to 1 if you have the 'tcsetpgrp' function. */
#undef HAVE_TCSETPGRP

/* Define to 1 if you have the 'tempnam' function. */
#undef HAVE_TEMPNAM

/* Define to 1 if you have the <termios.h> header file. */
#undef HAVE_TERMIOS_H

/* Define to 1 if you have the <term.h> header file. */
#undef HAVE_TERM_H

/* Define to 1 if you have the 'timegm' function. */
#undef HAVE_TIMEGM

/* Define if you have the 'timerfd_create' function. */
#undef HAVE_TIMERFD_CREATE

/* Define to 1 if you have the 'times' function. */
#undef HAVE_TIMES

/* Define to 1 if you have the 'tmpfile' function. */
#undef HAVE_TMPFILE

/* Define to 1 if you have the 'tmpnam' function. */
#undef HAVE_TMPNAM

/* Define to 1 if you have the 'tmpnam_r' function. */
#undef HAVE_TMPNAM_R

/* Define to 1 if your 'struct tm' has 'tm_zone'. Deprecated, use
   'HAVE_STRUCT_TM_TM_ZONE' instead. */
#undef HAVE_TM_ZONE

/* Define to 1 if you have the 'truncate' function. */
#undef HAVE_TRUNCATE

/* Define to 1 if you have the 'ttyname' function. */
#undef HAVE_TTYNAME

/* Define to 1 if you don't have 'tm_zone' but do have the external array
   'tzname'. */
#undef HAVE_TZNAME

/* Define to 1 if you have the 'umask' function. */
#undef HAVE_UMASK

/* Define to 1 if you have the 'uname' function. */
#undef HAVE_UNAME

/* Define to 1 if you have the <unistd.h> header file. */
#undef HAVE_UNISTD_H

/* Define to 1 if you have the 'unlinkat' function. */
#undef HAVE_UNLINKAT

/* Define to 1 if you have the 'unlockpt' function. */
#undef HAVE_UNLOCKPT

/* Define to 1 if you have the 'unshare' function. */
#undef HAVE_UNSHARE

/* Define if you have a useable wchar_t type defined in wchar.h; useable means
   wchar_t must be an unsigned type with at least 16 bits. (see
   Include/unicodeobject.h). */
#undef HAVE_USABLE_WCHAR_T

/* Define to 1 if you have the <util.h> header file. */
#undef HAVE_UTIL_H

/* Define to 1 if you have the 'utimensat' function. */
#undef HAVE_UTIMENSAT

/* Define to 1 if you have the 'utimes' function. */
#undef HAVE_UTIMES

/* Define to 1 if you have the <utime.h> header file. */
#undef HAVE_UTIME_H

/* Define to 1 if you have the <utmp.h> header file. */
#undef HAVE_UTMP_H

/* Define to 1 if you have the 'uuid_create' function. */
#undef HAVE_UUID_CREATE

/* Define to 1 if you have the 'uuid_enc_be' function. */
#undef HAVE_UUID_ENC_BE

/* Define if uuid_generate_time_safe() exists. */
#undef HAVE_UUID_GENERATE_TIME_SAFE

/* Define to 1 if you have the <uuid.h> header file. */
#undef HAVE_UUID_H

/* Define to 1 if you have the <uuid/uuid.h> header file. */
#undef HAVE_UUID_UUID_H

/* Define to 1 if you have the 'vfork' function. */
#undef HAVE_VFORK

/* Define to 1 if you have the 'wait' function. */
#undef HAVE_WAIT

/* Define to 1 if you have the 'wait3' function. */
#undef HAVE_WAIT3

/* Define to 1 if you have the 'wait4' function. */
#undef HAVE_WAIT4

/* Define to 1 if you have the 'waitid' function. */
#undef HAVE_WAITID

/* Define to 1 if you have the 'waitpid' function. */
#undef HAVE_WAITPID

/* Define if the compiler provides a wchar.h header file. */
#undef HAVE_WCHAR_H

/* Define to 1 if you have the 'wcscoll' function. */
#undef HAVE_WCSCOLL

/* Define to 1 if you have the 'wcsftime' function. */
#undef HAVE_WCSFTIME

/* Define to 1 if you have the 'wcsxfrm' function. */
#undef HAVE_WCSXFRM

/* Define to 1 if you have the 'wmemcmp' function. */
#undef HAVE_WMEMCMP

/* Define if tzset() actually switches the local timezone in a meaningful way.
   */
#undef HAVE_WORKING_TZSET

/* Define to 1 if you have the 'writev' function. */
#undef HAVE_WRITEV

/* Define if the zlib library has inflateCopy */
#undef HAVE_ZLIB_COPY

/* Define to 1 if you have the <zlib.h> header file. */
#undef HAVE_ZLIB_H

/* Define to 1 if you have the '_getpty' function. */
#undef HAVE__GETPTY

/* Define to 1 if the system has the type '__uint128_t'. */
#undef HAVE___UINT128_T

/* Define to 1 if 'major', 'minor', and 'makedev' are declared in <mkdev.h>.
   */
#undef MAJOR_IN_MKDEV

/* Define to 1 if 'major', 'minor', and 'makedev' are declared in
   <sysmacros.h>. */
#undef MAJOR_IN_SYSMACROS

/* Define if mvwdelch in curses.h is an expression. */
#undef MVWDELCH_IS_EXPRESSION

/* Define to the address where bug reports for this package should be sent. */
#undef PACKAGE_BUGREPORT

/* Define to the full name of this package. */
#undef PACKAGE_NAME

/* Define to the full name and version of this package. */
#undef PACKAGE_STRING

/* Define to the one symbol short name of this package. */
#undef PACKAGE_TARNAME

/* Define to the home page for this package. */
#undef PACKAGE_URL

/* Define to the version of this package. */
#undef PACKAGE_VERSION

/* Define if POSIX semaphores aren't enabled on your system */
#undef POSIX_SEMAPHORES_NOT_ENABLED

/* Define if pthread_key_t is compatible with int. */
#undef PTHREAD_KEY_T_IS_COMPATIBLE_WITH_INT

/* Defined if PTHREAD_SCOPE_SYSTEM supported. */
#undef PTHREAD_SYSTEM_SCHED_SUPPORTED

/* Define as the preferred size in bits of long digits */
#undef PYLONG_BITS_IN_DIGIT

/* Maximum length in bytes of a thread name */
#undef PYTHREAD_NAME_MAXLEN

/* enabled builtin hash modules */
#undef PY_BUILTIN_HASHLIB_HASHES

/* Define if you want to coerce the C locale to a UTF-8 based locale */
#undef PY_COERCE_C_LOCALE

/* Define to 1 if you have the perf trampoline. */
#undef PY_HAVE_PERF_TRAMPOLINE

/* Define to 1 to build the sqlite module with loadable extensions support. */
#undef PY_SQLITE_ENABLE_LOAD_EXTENSION

/* Define if SQLite was compiled with the serialize API */
#undef PY_SQLITE_HAVE_SERIALIZE

/* Default cipher suites list for ssl module. 1: Python's preferred selection,
   2: leave OpenSSL defaults untouched, 0: custom string */
#undef PY_SSL_DEFAULT_CIPHERS

/* Cipher suite string for PY_SSL_DEFAULT_CIPHERS=0 */
#undef PY_SSL_DEFAULT_CIPHER_STRING

/* PEP 11 Support tier (1, 2, 3 or 0 for unsupported) */
#undef PY_SUPPORT_TIER

/* Define if you want to build an interpreter with many run-time checks. */
#undef Py_DEBUG

/* Defined if Python is built as a shared library. */
#undef Py_ENABLE_SHARED

/* Defined if _Complex C type can be used with libffi. */
#undef Py_FFI_SUPPORT_C_COMPLEX

/* Define if you want to disable the GIL */
#undef Py_GIL_DISABLED

/* Define hash algorithm for str, bytes and memoryview. SipHash24: 1, FNV: 2,
   SipHash13: 3, externally defined: 0 */
#undef Py_HASH_ALGORITHM

/* Defined if _Complex C type is available. */
#undef Py_HAVE_C_COMPLEX

/* Define if year with century should be normalized for strftime. */
#undef Py_NORMALIZE_CENTURY

/* Define if rl_startup_hook takes arguments */
#undef Py_RL_STARTUP_HOOK_TAKES_ARGS

/* Define if you want to enable internal statistics gathering. */
#undef Py_STATS

/* The version of SunOS/Solaris as reported by `uname -r' without the dot. */
#undef Py_SUNOS_VERSION

/* Define if you want to enable tracing references for debugging purpose */
#undef Py_TRACE_REFS

/* assume C89 semantics that RETSIGTYPE is always void */
#undef RETSIGTYPE

/* Define if setpgrp() must be called as setpgrp(0, 0). */
#undef SETPGRP_HAVE_ARG

/* Define if i>>j for signed int i does not extend the sign bit when i < 0 */
#undef SIGNED_RIGHT_SHIFT_ZERO_FILLS

/* The size of 'double', as computed by sizeof. */
#undef SIZEOF_DOUBLE

/* The size of 'float', as computed by sizeof. */
#undef SIZEOF_FLOAT

/* The size of 'fpos_t', as computed by sizeof. */
#undef SIZEOF_FPOS_T

/* The size of 'int', as computed by sizeof. */
#undef SIZEOF_INT

/* The size of 'long', as computed by sizeof. */
#undef SIZEOF_LONG

/* The size of 'long double', as computed by sizeof. */
#undef SIZEOF_LONG_DOUBLE

/* The size of 'long long', as computed by sizeof. */
#undef SIZEOF_LONG_LONG

/* The size of 'off_t', as computed by sizeof. */
#undef SIZEOF_OFF_T

/* The size of 'pid_t', as computed by sizeof. */
#undef SIZEOF_PID_T

/* The size of 'pthread_key_t', as computed by sizeof. */
#undef SIZEOF_PTHREAD_KEY_T

/* The size of 'pthread_t', as computed by sizeof. */
#undef SIZEOF_PTHREAD_T

/* The size of 'short', as computed by sizeof. */
#undef SIZEOF_SHORT

/* The size of 'size_t', as computed by sizeof. */
#undef SIZEOF_SIZE_T

/* The size of 'time_t', as computed by sizeof. */
#undef SIZEOF_TIME_T

/* The size of 'uintptr_t', as computed by sizeof. */
#undef SIZEOF_UINTPTR_T

/* The size of 'void *', as computed by sizeof. */
#undef SIZEOF_VOID_P

/* The size of 'wchar_t', as computed by sizeof. */
#undef SIZEOF_WCHAR_T

/* The size of '_Bool', as computed by sizeof. */
#undef SIZEOF__BOOL

/* Define to 1 if you have the ANSI C header files. */
#undef STDC_HEADERS

/* Define if you can safely include both <sys/select.h> and <sys/time.h>
   (which you can't on SCO ODT 3.0). */
#undef SYS_SELECT_WITH_SYS_TIME

/* Custom thread stack size depending on chosen sanitizer runtimes. */
#undef THREAD_STACK_SIZE

/* Library needed by timemodule.c: librt may be needed for clock_gettime() */
#undef TIMEMODULE_LIB

/* Define to 1 if your <sys/time.h> declares 'struct tm'. */
#undef TM_IN_SYS_TIME

/* Define if you want to use computed gotos in ceval.c. */
#undef USE_COMPUTED_GOTOS

/* Enable extensions on AIX, Interix, z/OS.  */
#ifndef _ALL_SOURCE
# undef _ALL_SOURCE
#endif
/* Enable general extensions on macOS.  */
#ifndef _DARWIN_C_SOURCE
# undef _DARWIN_C_SOURCE
#endif
/* Enable general extensions on Solaris.  */
#ifndef __EXTENSIONS__
# undef __EXTENSIONS__
#endif
/* Enable GNU extensions on systems that have them.  */
#ifndef _GNU_SOURCE
# undef _GNU_SOURCE
#endif
/* Enable X/Open compliant socket functions that do not require linking
   with -lxnet on HP-UX 11.11.  */
#ifndef _HPUX_ALT_XOPEN_SOCKET_API
# undef _HPUX_ALT_XOPEN_SOCKET_API
#endif
/* Identify the host operating system as Minix.
   This macro does not affect the system headers' behavior.
   A future release of Autoconf may stop defining this macro.  */
#ifndef _MINIX
# undef _MINIX
#endif
/* Enable general extensions on NetBSD.
   Enable NetBSD compatibility extensions on Minix.  */
#ifndef _NETBSD_SOURCE
# undef _NETBSD_SOURCE
#endif
/* Enable OpenBSD compatibility extensions on NetBSD.
   Oddly enough, this does nothing on OpenBSD.  */
#ifndef _OPENBSD_SOURCE
# undef _OPENBSD_SOURCE
#endif
/* Define to 1 if needed for POSIX-compatible behavior.  */
#ifndef _POSIX_SOURCE
# undef _POSIX_SOURCE
#endif
/* Define to 2 if needed for POSIX-compatible behavior.  */
#ifndef _POSIX_1_SOURCE
# undef _POSIX_1_SOURCE
#endif
/* Enable POSIX-compatible threading on Solaris.  */
#ifndef _POSIX_PTHREAD_SEMANTICS
# undef _POSIX_PTHREAD_SEMANTICS
#endif
/* Enable extensions specified by ISO/IEC TS 18661-5:2014.  */
#ifndef __STDC_WANT_IEC_60559_ATTRIBS_EXT__
# undef __STDC_WANT_IEC_60559_ATTRIBS_EXT__
#endif
/* Enable extensions specified by ISO/IEC TS 18661-1:2014.  */
#ifndef __STDC_WANT_IEC_60559_BFP_EXT__
# undef __STDC_WANT_IEC_60559_BFP_EXT__
#endif
/* Enable extensions specified by ISO/IEC TS 18661-2:2015.  */
#ifndef __STDC_WANT_IEC_60559_DFP_EXT__
# undef __STDC_WANT_IEC_60559_DFP_EXT__
#endif
/* Enable extensions specified by C23 Annex F.  */
#ifndef __STDC_WANT_IEC_60559_EXT__
# undef __STDC_WANT_IEC_60559_EXT__
#endif
/* Enable extensions specified by ISO/IEC TS 18661-4:2015.  */
#ifndef __STDC_WANT_IEC_60559_FUNCS_EXT__
# undef __STDC_WANT_IEC_60559_FUNCS_EXT__
#endif
/* Enable extensions specified by C23 Annex H and ISO/IEC TS 18661-3:2015.  */
#ifndef __STDC_WANT_IEC_60559_TYPES_EXT__
# undef __STDC_WANT_IEC_60559_TYPES_EXT__
#endif
/* Enable extensions specified by ISO/IEC TR 24731-2:2010.  */
#ifndef __STDC_WANT_LIB_EXT2__
# undef __STDC_WANT_LIB_EXT2__
#endif
/* Enable extensions specified by ISO/IEC 24747:2009.  */
#ifndef __STDC_WANT_MATH_SPEC_FUNCS__
# undef __STDC_WANT_MATH_SPEC_FUNCS__
#endif
/* Enable extensions on HP NonStop.  */
#ifndef _TANDEM_SOURCE
# undef _TANDEM_SOURCE
#endif
/* Enable X/Open extensions.  Define to 500 only if necessary
   to make mbstate_t available.  */
#ifndef _XOPEN_SOURCE
# undef _XOPEN_SOURCE
#endif


/* Define if WINDOW in curses.h offers a field _flags. */
#undef WINDOW_HAS_FLAGS

/* Define if you want build the _decimal module using a coroutine-local rather
   than a thread-local context */
#undef WITH_DECIMAL_CONTEXTVAR

/* Define if you want documentation strings in extension modules */
#undef WITH_DOC_STRINGS

/* Define if you want to compile in DTrace support */
#undef WITH_DTRACE

/* Define if you want to use the new-style (Openstep, Rhapsody, MacOS) dynamic
   linker (dyld) instead of the old-style (NextStep) dynamic linker (rld).
   Dyld is necessary to support frameworks. */
#undef WITH_DYLD

/* Define to build the readline module against libedit. */
#undef WITH_EDITLINE

/* Define to 1 if libintl is needed for locale functions. */
#undef WITH_LIBINTL

/* Define if you want to compile in mimalloc memory allocator. */
#undef WITH_MIMALLOC

/* Define if you want to produce an OpenStep/Rhapsody framework (shared
   library plus accessory files). */
#undef WITH_NEXT_FRAMEWORK

/* Define if you want to compile in Python-specific mallocs */
#undef WITH_PYMALLOC

/* Define if you want pymalloc to be disabled when running under valgrind */
#undef WITH_VALGRIND

/* Define WORDS_BIGENDIAN to 1 if your processor stores words with the most
   significant byte first (like Motorola and SPARC, unlike Intel). */
#if defined AC_APPLE_UNIVERSAL_BUILD
# if defined __BIG_ENDIAN__
#  define WORDS_BIGENDIAN 1
# endif
#else
# ifndef WORDS_BIGENDIAN
#  undef WORDS_BIGENDIAN
# endif
#endif

/* Define if arithmetic is subject to x87-style double rounding issue */
#undef X87_DOUBLE_ROUNDING

/* Define on OpenBSD to activate all library features */
#undef _BSD_SOURCE

/* Define on Darwin to activate all library features */
#undef _DARWIN_C_SOURCE

/* This must be set to 64 on some systems to enable large file support. */
#undef _FILE_OFFSET_BITS

/* Define to include mbstate_t for mbrtowc */
#undef _INCLUDE__STDC_A1_SOURCE

/* This must be defined on some systems to enable large file support. */
#undef _LARGEFILE_SOURCE

/* This must be defined on AIX systems to enable large file support. */
#undef _LARGE_FILES

/* Define on NetBSD to activate all library features */
#undef _NETBSD_SOURCE

/* Define to activate features from IEEE Stds 1003.1-2008 */
#undef _POSIX_C_SOURCE

/* Define if you have POSIX threads, and your system does not define that. */
#undef _POSIX_THREADS

/* framework name */
#undef _PYTHONFRAMEWORK

/* Define to force use of thread-safe errno, h_errno, and other functions */
#undef _REENTRANT

/* Define to 1 if you want to emulate getpid() on WASI */
#undef _WASI_EMULATED_GETPID

/* Define to 1 if you want to emulate process clocks on WASI */
#undef _WASI_EMULATED_PROCESS_CLOCKS

/* Define to 1 if you want to emulate signals on WASI */
#undef _WASI_EMULATED_SIGNAL

/* Define to the level of X/Open that your system supports */
#undef _XOPEN_SOURCE

/* Define to activate Unix95-and-earlier features */
#undef _XOPEN_SOURCE_EXTENDED

/* Define on FreeBSD to activate all library features */
#undef __BSD_VISIBLE

/* Define to 'long' if <time.h> does not define clock_t. */
#undef clock_t

/* Define to empty if 'const' does not conform to ANSI C. */
#undef const

/* Define as 'int' if <sys/types.h> doesn't define. */
#undef gid_t

/* Define to 'int' if <sys/types.h> does not define. */
#undef mode_t

/* Define to 'long int' if <sys/types.h> does not define. */
#undef off_t

/* Define as a signed integer type capable of holding a process identifier. */
#undef pid_t

/* Define to empty if the keyword does not work. */
#undef signed

/* Define as 'unsigned int' if <stddef.h> doesn't define. */
#undef size_t

/* Define to 'int' if <sys/socket.h> does not define. */
#undef socklen_t

/* Define as 'int' if <sys/types.h> doesn't define. */
#undef uid_t


/* Define the macros needed if on a UnixWare 7.x system. */
#if defined(__USLC__) && defined(__SCO_VERSION__)
#define STRICT_SYSV_CURSES /* Don't use ncurses extensions */
#endif

#endif /*Py_PYCONFIG_H*/

