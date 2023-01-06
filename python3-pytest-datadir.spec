#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	pytest plugin for test data directories and files
Summary(pl.UTF-8):	Wtyczka pytesta do katalogów i plików z danymi testowymi
Name:		python3-pytest-datadir
Version:	1.4.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-datadir/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-datadir/pytest-datadir-%{version}.tar.gz
# Source0-md5:	d5043376db09d710e24a71b96026d728
URL:		https://pypi.org/project/pytest-datadir/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 5.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest plugin for manipulating test data directories and files.

%description -l pl.UTF-8
Wtyczka pytesta do operowania na katalogach i plikach z danymi
testowymi.

%prep
%setup -q -n pytest-datadir-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_datadir.plugin" \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.rst LICENSE README.md
%{py3_sitescriptdir}/pytest_datadir
%{py3_sitescriptdir}/pytest_datadir-%{version}-py*.egg-info
