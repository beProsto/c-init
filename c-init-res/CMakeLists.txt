# minimum version of cmake this will work on
cmake_minimum_required(VERSION 3.0.0)

# project name Major.Minor.Patch
project({name} VERSION 1.0.0)

# include_directories and link_libraries work on all targets defined BELOW them
# translates to -Iinclude
include_directories(include)

# recursively search the include and src directories
file(GLOB_RECURSE srcs
	"include/*.hpp"
	"include/*.h"
	"src/*.cpp"
	"src/*.c"
)
{LIB_SNIPPET_START}
# depending on the library type, we set a correct macro
# create a library of of the sources
if(LIBTYPE STREQUAL "STATIC")
	add_library({name} STATIC ${srcs})
	target_compile_definitions({name} PRIVATE LIB_BUILD_STATIC)

else()
	add_library({name} SHARED ${srcs})
	target_compile_definitions({name} PRIVATE LIB_BUILD_SHARED)

endif()
{LIB_SNIPPET_END}{APP_SNIPPET_START}
# create an executable app out of the sources
add_executable({name} ${srcs})
{APP_SNIPPET_END}
# cmake's ez :D