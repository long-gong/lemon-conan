from conans import ConanFile, CMake, tools


class LemonConan(ConanFile):
    name = "Lemon"
    version = "1.3.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "https://lemon.cs.elte.hu/trac/lemon"
    description = "LEMON stands for Library for Efficient Modeling and Optimization in Networks. It is a C++ template library providing efficient implementations of common data structures and algorithms with focus on combinatorial optimization tasks connected mainly with graphs and networks."
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("wget http://lemon.cs.elte.hu/pub/sources/lemon-1.3.1.tar.gz")
        self.run("tar -zxvf lemon-1.3.1.tar.gz")
        tools.replace_in_file("lemon-1.3.1/CMakeLists.txt", "PROJECT(${PROJECT_NAME})",
                              '''PROJECT(${PROJECT_NAME})
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="lemon-1.3.1")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="lemon-1.3.1")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["emon"]
