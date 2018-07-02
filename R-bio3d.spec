#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bio3d
Version  : 2.3.4
Release  : 2
URL      : https://cran.r-project.org/src/contrib/bio3d_2.3-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bio3d_2.3-4.tar.gz
Summary  : Biological Structure Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bio3d-lib
Requires: R-Rcpp
Requires: R-igraph
Requires: R-markdown
Requires: R-stringi
BuildRequires : R-Rcpp
BuildRequires : R-igraph
BuildRequires : R-markdown
BuildRequires : R-stringi
BuildRequires : clr-R-helpers
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
sequence and dynamics data. Features include the ability to read and write
    structure, sequence and dynamic trajectory data, perform sequence and structure
    database searches, data summaries, atom selection, alignment, superposition,
    rigid core identification, clustering, torsion analysis, distance matrix
    analysis, structure and sequence conservation analysis, normal mode analysis,
    principal component analysis of heterogeneous structure data, and correlation
    network analysis from normal mode and molecular dynamics data. In addition,
    various utility functions are provided to enable the statistical and graphical
    power of the R environment to work with biological sequence and structural data.
    Please refer to the URLs below for more information.

%package lib
Summary: lib components for the R-bio3d package.
Group: Libraries

%description lib
lib components for the R-bio3d package.


%prep
%setup -q -c -n bio3d

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530308328

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530308328
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bio3d
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bio3d
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bio3d
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bio3d|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bio3d/CITATION
/usr/lib64/R/library/bio3d/DESCRIPTION
/usr/lib64/R/library/bio3d/INDEX
/usr/lib64/R/library/bio3d/Meta/Rd.rds
/usr/lib64/R/library/bio3d/Meta/data.rds
/usr/lib64/R/library/bio3d/Meta/demo.rds
/usr/lib64/R/library/bio3d/Meta/features.rds
/usr/lib64/R/library/bio3d/Meta/hsearch.rds
/usr/lib64/R/library/bio3d/Meta/links.rds
/usr/lib64/R/library/bio3d/Meta/nsInfo.rds
/usr/lib64/R/library/bio3d/Meta/package.rds
/usr/lib64/R/library/bio3d/Meta/vignette.rds
/usr/lib64/R/library/bio3d/NAMESPACE
/usr/lib64/R/library/bio3d/NEWS
/usr/lib64/R/library/bio3d/R/bio3d
/usr/lib64/R/library/bio3d/R/bio3d.rdb
/usr/lib64/R/library/bio3d/R/bio3d.rdx
/usr/lib64/R/library/bio3d/data/Rdata.rdb
/usr/lib64/R/library/bio3d/data/Rdata.rds
/usr/lib64/R/library/bio3d/data/Rdata.rdx
/usr/lib64/R/library/bio3d/demo/md.R
/usr/lib64/R/library/bio3d/demo/nma.R
/usr/lib64/R/library/bio3d/demo/pca.R
/usr/lib64/R/library/bio3d/demo/pdb.R
/usr/lib64/R/library/bio3d/doc/bio3d_vignettes.Rmd
/usr/lib64/R/library/bio3d/doc/bio3d_vignettes.html
/usr/lib64/R/library/bio3d/doc/index.html
/usr/lib64/R/library/bio3d/examples/1dpx.pdb
/usr/lib64/R/library/bio3d/examples/1hel.pdb
/usr/lib64/R/library/bio3d/examples/aspirin.mol2
/usr/lib64/R/library/bio3d/examples/crambin.inpcrd
/usr/lib64/R/library/bio3d/examples/crambin.prmtop
/usr/lib64/R/library/bio3d/examples/hivp.dcd
/usr/lib64/R/library/bio3d/examples/hivp.pdb
/usr/lib64/R/library/bio3d/examples/hivp_xray.fa
/usr/lib64/R/library/bio3d/examples/kif1a.fa
/usr/lib64/R/library/bio3d/examples/test.pdb
/usr/lib64/R/library/bio3d/examples/transducin.fa
/usr/lib64/R/library/bio3d/help/AnIndex
/usr/lib64/R/library/bio3d/help/aliases.rds
/usr/lib64/R/library/bio3d/help/bio3d.rdb
/usr/lib64/R/library/bio3d/help/bio3d.rdx
/usr/lib64/R/library/bio3d/help/paths.rds
/usr/lib64/R/library/bio3d/html/00Index.html
/usr/lib64/R/library/bio3d/html/R.css
/usr/lib64/R/library/bio3d/libs/symbols.rds
/usr/lib64/R/library/bio3d/matrices/bio3d.mat
/usr/lib64/R/library/bio3d/matrices/blosum62.mat
/usr/lib64/R/library/bio3d/matrices/custom.mat
/usr/lib64/R/library/bio3d/matrices/emboss_properties.mat
/usr/lib64/R/library/bio3d/matrices/pam30.mat
/usr/lib64/R/library/bio3d/matrices/properties.mat
/usr/lib64/R/library/bio3d/matrices/similarity.mat
/usr/lib64/R/library/bio3d/staticdocs/index.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bio3d/libs/bio3d.so
/usr/lib64/R/library/bio3d/libs/bio3d.so.avx2
/usr/lib64/R/library/bio3d/libs/bio3d.so.avx512
