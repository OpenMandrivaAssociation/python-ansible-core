Name:		python-ansible-core
Version:	2.21.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/ansible_core/ansible_core-%{version}.tar.gz
Summary:	Radically simple IT automation
URL:		https://pypi.org/project/ansible-core/
License:	None
Group:		Development/Python
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildArch:	noarch

%patchlist
# dropped (no longer applies): ansible-core-2.21.2-resolvelib-1.1.patch

%description
Radically simple IT automation

%prep
%autosetup -p1 -n ansible_core-2.21.2

%files
%{_bindir}/ansible*
%{py_sitedir}/ansible
%{py_sitedir}/ansible_test
%{py_sitedir}/ansible_core-*.*-info
