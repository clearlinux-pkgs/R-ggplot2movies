#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ggplot2movies
Version  : 0.0.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/ggplot2movies_0.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggplot2movies_0.0.1.tar.gz
Summary  : Movies Data
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n ggplot2movies

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552923199

%install
export SOURCE_DATE_EPOCH=1552923199
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggplot2movies
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggplot2movies
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggplot2movies
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  ggplot2movies || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggplot2movies/DESCRIPTION
/usr/lib64/R/library/ggplot2movies/INDEX
/usr/lib64/R/library/ggplot2movies/Meta/Rd.rds
/usr/lib64/R/library/ggplot2movies/Meta/data.rds
/usr/lib64/R/library/ggplot2movies/Meta/features.rds
/usr/lib64/R/library/ggplot2movies/Meta/hsearch.rds
/usr/lib64/R/library/ggplot2movies/Meta/links.rds
/usr/lib64/R/library/ggplot2movies/Meta/nsInfo.rds
/usr/lib64/R/library/ggplot2movies/Meta/package.rds
/usr/lib64/R/library/ggplot2movies/NAMESPACE
/usr/lib64/R/library/ggplot2movies/R/ggplot2movies
/usr/lib64/R/library/ggplot2movies/R/ggplot2movies.rdb
/usr/lib64/R/library/ggplot2movies/R/ggplot2movies.rdx
/usr/lib64/R/library/ggplot2movies/data/Rdata.rdb
/usr/lib64/R/library/ggplot2movies/data/Rdata.rds
/usr/lib64/R/library/ggplot2movies/data/Rdata.rdx
/usr/lib64/R/library/ggplot2movies/help/AnIndex
/usr/lib64/R/library/ggplot2movies/help/aliases.rds
/usr/lib64/R/library/ggplot2movies/help/ggplot2movies.rdb
/usr/lib64/R/library/ggplot2movies/help/ggplot2movies.rdx
/usr/lib64/R/library/ggplot2movies/help/paths.rds
/usr/lib64/R/library/ggplot2movies/html/00Index.html
/usr/lib64/R/library/ggplot2movies/html/R.css
