cmake_minimum_required(VERSION 3.10.2)

project(SinglephaseChanAndVeseDenseFieldLevelSetSegmentation)

find_package(ITK REQUIRED)
include(${ITK_USE_FILE})


add_executable(SinglephaseChanAndVeseDenseFieldLevelSetSegmentation Code.cxx)
target_link_libraries(SinglephaseChanAndVeseDenseFieldLevelSetSegmentation ${ITK_LIBRARIES})

install(TARGETS SinglephaseChanAndVeseDenseFieldLevelSetSegmentation
  DESTINATION bin/ITKSphinxExamples/Nonunit/Review
  COMPONENT Runtime
  )

install(FILES Code.cxx CMakeLists.txt
  DESTINATION share/ITKSphinxExamples/Code/Nonunit/Review/SinglephaseChanAndVeseDenseFieldLevelSetSegmentation/
  COMPONENT Code
  )


enable_testing()
add_test(NAME SinglephaseChanAndVeseDenseFieldLevelSetSegmentationTest
  COMMAND ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/SinglephaseChanAndVeseDenseFieldLevelSetSegmentation)
