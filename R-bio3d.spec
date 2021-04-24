#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bio3d
Version  : 2.4.1
Release  : 25
URL      : https://cran.r-project.org/src/contrib/bio3d_2.4-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bio3d_2.4-1.tar.gz
Summary  : Biological Structure Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bio3d-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
BuildRequires : pkgconfig(zlib)

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
cd %{_builddir}/bio3d

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589576556

%install
export SOURCE_DATE_EPOCH=1589576556
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bio3d
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bio3d
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bio3d || :


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
/usr/lib64/R/library/bio3d/matrices/bio3d.mat
/usr/lib64/R/library/bio3d/matrices/blosum62.mat
/usr/lib64/R/library/bio3d/matrices/custom.mat
/usr/lib64/R/library/bio3d/matrices/emboss_properties.mat
/usr/lib64/R/library/bio3d/matrices/pam30.mat
/usr/lib64/R/library/bio3d/matrices/properties.mat
/usr/lib64/R/library/bio3d/matrices/similarity.mat
/usr/lib64/R/library/bio3d/staticdocs/index.r
/usr/lib64/R/library/bio3d/tests/testthat.R
/usr/lib64/R/library/bio3d/tests/testthat/test-aa2mass.R
/usr/lib64/R/library/bio3d/tests/testthat/test-aanma.R
/usr/lib64/R/library/bio3d/tests/testthat/test-aanma.pdbs.R
/usr/lib64/R/library/bio3d/tests/testthat/test-atom.select.R
/usr/lib64/R/library/bio3d/tests/testthat/test-atom2mass.R
/usr/lib64/R/library/bio3d/tests/testthat/test-clean.pdb.R
/usr/lib64/R/library/bio3d/tests/testthat/test-cmap.R
/usr/lib64/R/library/bio3d/tests/testthat/test-cna.R
/usr/lib64/R/library/bio3d/tests/testthat/test-core.find.R
/usr/lib64/R/library/bio3d/tests/testthat/test-dccm.R
/usr/lib64/R/library/bio3d/tests/testthat/test-deformation.R
/usr/lib64/R/library/bio3d/tests/testthat/test-dssp.R
/usr/lib64/R/library/bio3d/tests/testthat/test-fitting.R
/usr/lib64/R/library/bio3d/tests/testthat/test-get.pdb.R
/usr/lib64/R/library/bio3d/tests/testthat/test-get.seq.R
/usr/lib64/R/library/bio3d/tests/testthat/test-gnm.R
/usr/lib64/R/library/bio3d/tests/testthat/test-mol2.R
/usr/lib64/R/library/bio3d/tests/testthat/test-nma.R
/usr/lib64/R/library/bio3d/tests/testthat/test-nma.pdbs.R
/usr/lib64/R/library/bio3d/tests/testthat/test-overlap.R
/usr/lib64/R/library/bio3d/tests/testthat/test-pca.R
/usr/lib64/R/library/bio3d/tests/testthat/test-pdb.annotate.R
/usr/lib64/R/library/bio3d/tests/testthat/test-pdbsplit.R
/usr/lib64/R/library/bio3d/tests/testthat/test-read.all.R
/usr/lib64/R/library/bio3d/tests/testthat/test-read.cif.R
/usr/lib64/R/library/bio3d/tests/testthat/test-read.ncdf.R
/usr/lib64/R/library/bio3d/tests/testthat/test-read.pdb.R
/usr/lib64/R/library/bio3d/tests/testthat/test-rmsd.R
/usr/lib64/R/library/bio3d/tests/testthat/test-seqaln.R
/usr/lib64/R/library/bio3d/tests/testthat/test-vector-funs.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bio3d/libs/bio3d.so
