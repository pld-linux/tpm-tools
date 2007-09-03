Summary:	Management tools for the TPM hardware
Summary(pl.UTF-8):	Narzędzia zarządzające sprzętem TPM
Name:		tpm-tools
Version:	1.2.5.1
Release:	1
License:	CPL v1+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/trousers/%{name}-%{version}.tar.gz
# Source0-md5:	621a354f2b054646bbb15cfd4a5270b7
URL:		http://trousers.sourceforge.net/
BuildRequires:	opencryptoki-devel >= 2.2.4
BuildRequires:	openssl-devel
BuildRequires:	trousers-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tpm-tools is a group of tools to manage and utilize the Trusted
Computing Group's TPM hardware. TPM hardware can create, store and use
RSA keys securely (without ever being exposed in memory), verify a
platform's software state using cryptographic hashes and more.

%description -l pl.UTF-8
tpm-tools to grupa narzędzi do zarządzania i wykorzystywania sprzętu
TPM opracowanego przez Trusted Computing Group. Sprzęt TPM potrafi
tworzyć, przechowywać i wykorzystywać klucze RSA w sposób bezpieczny
(bez ujawniania ich kiedykolwiek w pamięci), weryfikować stan
oprogramowania przy użyciu skrótów kryptograficznych itp.

%package devel
Summary:	Header files for tpm_unseal library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tpm_unseal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	trousers-devel

%description devel
Header files for tpm_unseal library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tpm_unseal.

%package static
Summary:	Static tpm_unseal library
Summary(pl.UTF-8):	Statyczna biblioteka tpm_unseal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tpm_unseal library.

%description static -l pl.UTF-8
Statyczna biblioteka tpm_unseal.

%package pkcs11
Summary:	Data management tools that use a PKCS#11 interface to the TPM
Summary(pl.UTF-8):	Narzędzia do zarządzania danymi wykorzystujace interfejs PKCS#11 do TPM
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	opencryptoki >= 2.2.4

%description pkcs11
tpm-tools-pkcs11 is a group of tools that uses the TPM PKCS#11 token
developed in the opencryptoki project. All data contained in the
PKCS#11 data store is protected by the TPM (keys, certificates, etc.).
You can import keys and certificates, list out the objects in the data
store, and protect data.

%description pkcs11 -l pl.UTF-8
tpm-tools-pkcs11 to grupa narzędzi wykorzystujących token TPM PKCS#11
opracowany w ramach projektu opencryptoki. Wszystkie dane zawarte w
kontenerze PKCS#11 są chronione przez TPM (klucze, certyfikaty itp.).
Narzędzia pozwalają importować klucze i certyfikaty, wypisywać listę
obiektów w kontenerze i chronić dane.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/tpm_*
%attr(755,root,root) %{_sbindir}/tpm_*
%attr(755,root,root) %{_libdir}/libtpm_unseal.so.*.*.*
%{_mandir}/man1/tpm_*.1*
%{_mandir}/man8/tpm_*.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtpm_unseal.so
%{_libdir}/libtpm_unseal.la
%{_includedir}/tpm_tools
%{_mandir}/man3/tpmUnseal*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtpm_unseal.a

%files pkcs11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tpmtoken_*
%{_mandir}/man1/tpmtoken_*.1*
