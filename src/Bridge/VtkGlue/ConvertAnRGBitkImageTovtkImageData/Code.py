#!/usr/bin/env python

# Copyright NumFOCUS
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import itk

from distutils.version import StrictVersion as VS

if VS(itk.Version.GetITKVersion()) < VS("5.2.0"):
    print("ITK 5.2.0 is required.")
    sys.exit(1)

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " <InputFileName>")
    sys.exit(1)

imageFileName = sys.argv[1]

inputImage = itk.imread(imageFileName)

vtkImage = itk.image_to_vtk_image(inputImage)

print(vtkImage)
