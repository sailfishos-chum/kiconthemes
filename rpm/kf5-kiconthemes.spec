%global kf5_version 5.116.0

Name: opt-kf5-kiconthemes
Version: 5.116.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 3 integration module with icon themes

License: LGPLv2+ and GPLv2+
URL:     https://api.kde.org/frameworks/kiconthemes/

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-karchive-devel >= %{kf5_version}
BuildRequires: opt-kf5-kconfigwidgets-devel >= %{kf5_version}
BuildRequires: opt-kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-ki18n-devel >= %{kf5_version}
BuildRequires: opt-kf5-kitemviews-devel >= %{kf5_version}
BuildRequires: opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-kguiaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros

BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qtbase-private-devel
BuildRequires: opt-qt5-qtsvg-devel
BuildRequires: opt-qt5-qttools-devel
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-kf5-karchive
Requires: opt-kf5-kconfigwidgets
Requires: opt-kf5-kcoreaddons
Requires: opt-kf5-kitemviews
Requires: opt-kf5-kwidgetsaddons
Requires: opt-kf5-kguiaddons


%description
KDE Frameworks 5 Tier 3 integration module with icon themes

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/kiconthemes.*
%{_opt_kf5_bindir}/kiconfinder5
%{_opt_kf5_libdir}/libKF5IconThemes.so.*
%{_opt_kf5_qtplugindir}/iconengines/KIconEnginePlugin.so
%{_opt_kf5_qtplugindir}/designer/*5widgets.so
%{_opt_kf5_datadir}/locale/

%files devel

%{_opt_kf5_includedir}/KF5/KIconThemes/
%{_opt_kf5_libdir}/libKF5IconThemes.so
%{_opt_kf5_libdir}/cmake/KF5IconThemes/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KIconThemes.pri
