# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob
import os.path


class Hisat2(MakefilePackage):
    """HISAT2 is a fast and sensitive alignment program for mapping
       next-generation sequencing reads (whole-genome, transcriptome, and
       exome sequencing data) against the general human population (as well as
       against a single reference genome)."""

    homepage = "http://ccb.jhu.edu/software/hisat2"
    url      = "ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.1.0-source.zip"

    version('2.1.0', '8b566d1b7e6c5801c8ae9824ed2da3d0')

    def install(self, spec, prefix):
        install_tree('doc', prefix.doc)
        install_tree('example', prefix.example)
        install_tree('hisatgenotype_modules', prefix.hisatgenotype_modules)
        install_tree('hisatgenotype_scripts', prefix.hisatgenotype_scripts)
        install_tree('scripts', prefix.scripts)
        mkdirp(prefix.bin)
        install('hisat2', prefix.bin)
        install('hisat2-align-s', prefix.bin)
        install('hisat2-align-l', prefix.bin)
        install('hisat2-build', prefix.bin)
        install('hisat2-build-s', prefix.bin)
        install('hisat2-build-l', prefix.bin)
        install('hisat2-inspect', prefix.bin)
        install('hisat2-inspect-s', prefix.bin)
        install('hisat2-inspect-l', prefix.bin)
        files = glob.iglob('*.py')
        for file in files:
            if os.path.isfile(file):
                install(file, prefix.bin)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', self.spec.prefix)
