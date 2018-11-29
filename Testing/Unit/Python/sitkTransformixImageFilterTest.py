from __future__ import print_function
import sys
import unittest


import SimpleITK as sitk


class TransformixImageFilterTest(unittest.TestCase):
    """Test the SimpleITK Process Object and related Command classes"""

    def setUp(self):
        pass

    def test_TransformixImageFilter_GetDeformationField(self):
    	  fixedImage = sitk.Image( 4, 4, sitk.sitkFloat32 )
    	  movingImage = sitk.Image( 4, 4, sitk.sitkFloat32 )
    	  fixedImage[0, 0] = movingImage[0, 0] = 1
    	  fixedImage[0, 1] = movingImage[0, 1] = 1
    	  fixedImage[1, 0] = movingImage[1, 0] = 1
    	  fixedImage[1, 1] = movingImage[1, 1] = 1

    	  movingImage.SetOrigin((1, 1))

    	  # Dummy registration
    	  elastixImageFilter = sitk.ElastixImageFilter()
    	  elastixImageFilter.SetParameter("MaximumNumberOfIterations", "10")
    	  elastixImageFilter.SetFixedImage(fixedImage)
    	  elastixImageFilter.SetMovingImage(movingImage)
    	  elastixImageFilter.Execute()

    	  transformixImageFilter = sitk.TransformixImageFilter()
    	  transformixImageFilter.SetTransformParameterMap(elastixImageFilter.GetTransformParameterMap())
    	  transformixImageFilter.ComputeDeformationFieldOn()
    	  transformixImageFilter.Execute()
    	  deformationField = transformixImageFilter.GetDeformationField()

if __name__ == '__main__':
    unittest.main()
