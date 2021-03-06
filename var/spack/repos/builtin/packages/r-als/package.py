# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RAls(RPackage):
    """Alternating least squares is often used to resolve components
    contributing to data with a bilinear structure; the basic
    technique may be extended to alternating constrained least squares.
    Commonly applied constraints include unimodality, non-negativity,
    and normalization of components. Several data matrices may be
    decomposed simultaneously by assuming that one of the two matrices
    in the bilinear decomposition is shared between datasets."""

    homepage = "https://cran.r-project.org/package=ALS"
    url      = "https://cran.rstudio.com/src/contrib/ALS_0.0.6.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/ALS"

    version('0.0.6', 'b72d97911e8ab7e4f8aed1a710b3d62d')

    depends_on('r-iso', type=('build', 'run'))
    depends_on('r-nnls', type=('build', 'run'))
