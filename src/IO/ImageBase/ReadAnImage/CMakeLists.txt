cmake_minimum_required(VERSION 3.10.2)

project( ReadAnImage )

find_package( ITK REQUIRED )
include( ${ITK_USE_FILE} )

add_executable( ReadAnImage Code.cxx )
target_link_libraries( ReadAnImage ${ITK_LIBRARIES} )

install( TARGETS ReadAnImage
  DESTINATION bin/ITKSphinxExamples/IO/ImageBase/
  COMPONENT Runtime
  )

install( FILES Code.cxx CMakeLists.txt
  DESTINATION share/ITKSphinxExamples/Code/IO/ImageBase/ReadAnImage
  COMPONENT Code
  )

enable_testing()
add_test( NAME ReadAnImageTest
  COMMAND ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ReadAnImage
    ${CMAKE_CURRENT_BINARY_DIR}/Yinyang.png
  )
