
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_java_awt_BitwiseXORComposite$GeneralContext__
#define __gnu_java_awt_BitwiseXORComposite$GeneralContext__

#pragma interface

#include <java/lang/Object.h>
extern "Java"
{
  namespace gnu
  {
    namespace java
    {
      namespace awt
      {
          class BitwiseXORComposite$GeneralContext;
      }
    }
  }
  namespace java
  {
    namespace awt
    {
        class Color;
      namespace image
      {
          class ColorModel;
          class Raster;
          class WritableRaster;
      }
    }
  }
}

class gnu::java::awt::BitwiseXORComposite$GeneralContext : public ::java::lang::Object
{

public:
  BitwiseXORComposite$GeneralContext(::java::awt::image::ColorModel *, ::java::awt::image::ColorModel *, ::java::awt::Color *);
  virtual void compose(::java::awt::image::Raster *, ::java::awt::image::Raster *, ::java::awt::image::WritableRaster *);
  virtual void dispose();
public: // actually package-private
  ::java::awt::image::ColorModel * __attribute__((aligned(__alignof__( ::java::lang::Object)))) srcColorModel;
  ::java::awt::image::ColorModel * dstColorModel;
  ::java::awt::Color * xorColor;
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_java_awt_BitwiseXORComposite$GeneralContext__
