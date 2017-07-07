from conans import ConanFile, CMake, tools
import os


class GslliteConan(ConanFile):
    name = "gsl-lite"
    version = "0.23.0"
    description = "GSL Lite: Guideline Support Library for C++98, C++11 up"
    license = "The MIT License (MIT)"
    url = "https://github.com/jorj1988/gsl-lite"
    generators = "cmake"
    exports_sources = "include/*"

    def package(self):
        self.copy(pattern="*", src="include", dst="include")
