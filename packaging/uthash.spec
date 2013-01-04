Name:           uthash
Version:        1.9.7
Release:        1
License:        BSD-style single-clause
Summary:        A hash table for C structures
Group:          System/Kernel
Source0:        %{name}-%{version}.tar.bz2

%description
Any C structure can be stored in a hash table using
uthash. Just add a UT_hash_handle to the structure
and choose one or more fields in your structure to
act as the key. Then use these macros to store,
retrieve or delete items from the hash table.

%package devel
Summary:        Development files for %name
Group:          Development/Libraries

%description devel
Development files for %name.

%prep
%setup -q
%build

%install

mkdir -p  %{buildroot}/usr/include
cd src
cp utarray.h uthash.h utlist.h utstring.h %{buildroot}/usr/include


%files devel
%defattr(-,root,root,-)
%{_includedir}/utarray.h
%{_includedir}/uthash.h
%{_includedir}/utlist.h
%{_includedir}/utstring.h

