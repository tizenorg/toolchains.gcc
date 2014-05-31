
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __javax_imageio_spi_ImageWriterSpi__
#define __javax_imageio_spi_ImageWriterSpi__

#pragma interface

#include <javax/imageio/spi/ImageReaderWriterSpi.h>
#include <gcj/array.h>

extern "Java"
{
  namespace java
  {
    namespace awt
    {
      namespace image
      {
          class RenderedImage;
      }
    }
  }
  namespace javax
  {
    namespace imageio
    {
        class ImageTypeSpecifier;
        class ImageWriter;
      namespace spi
      {
          class ImageWriterSpi;
      }
    }
  }
}

class javax::imageio::spi::ImageWriterSpi : public ::javax::imageio::spi::ImageReaderWriterSpi
{

public: // actually protected
  ImageWriterSpi();
public:
  ImageWriterSpi(::java::lang::String *, ::java::lang::String *, JArray< ::java::lang::String * > *, JArray< ::java::lang::String * > *, JArray< ::java::lang::String * > *, ::java::lang::String *, JArray< ::java::lang::Class * > *, JArray< ::java::lang::String * > *, jboolean, ::java::lang::String *, ::java::lang::String *, JArray< ::java::lang::String * > *, JArray< ::java::lang::String * > *, jboolean, ::java::lang::String *, ::java::lang::String *, JArray< ::java::lang::String * > *, JArray< ::java::lang::String * > *);
  virtual jboolean canEncodeImage(::javax::imageio::ImageTypeSpecifier *) = 0;
  virtual jboolean canEncodeImage(::java::awt::image::RenderedImage *);
  virtual ::javax::imageio::ImageWriter * createWriterInstance();
  virtual ::javax::imageio::ImageWriter * createWriterInstance(::java::lang::Object *) = 0;
  virtual JArray< ::java::lang::String * > * getImageReaderSpiNames();
  virtual JArray< ::java::lang::Class * > * getOutputTypes();
  virtual jboolean isFormatLossless();
  virtual jboolean isOwnWriter(::javax::imageio::ImageWriter *);
  static JArray< ::java::lang::Class * > * STANDARD_OUTPUT_TYPE;
public: // actually protected
  JArray< ::java::lang::Class * > * __attribute__((aligned(__alignof__( ::javax::imageio::spi::ImageReaderWriterSpi)))) outputTypes;
  JArray< ::java::lang::String * > * readerSpiNames;
public:
  static ::java::lang::Class class$;
};

#endif // __javax_imageio_spi_ImageWriterSpi__
