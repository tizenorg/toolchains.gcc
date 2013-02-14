
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_awt_xlib_XOffScreenImage__
#define __gnu_awt_xlib_XOffScreenImage__

#pragma interface

#include <java/awt/Image.h>
#include <gcj/array.h>

extern "Java"
{
  namespace gnu
  {
    namespace awt
    {
      namespace xlib
      {
          class XGraphicsConfiguration;
          class XOffScreenImage;
      }
    }
    namespace gcj
    {
      namespace xlib
      {
          class Drawable;
          class GC;
          class Pixmap;
      }
    }
  }
  namespace java
  {
    namespace awt
    {
        class Graphics;
        class GraphicsConfiguration;
      namespace image
      {
          class ColorModel;
          class ImageObserver;
          class ImageProducer;
      }
    }
  }
}

class gnu::awt::xlib::XOffScreenImage : public ::java::awt::Image
{

public: // actually package-private
  XOffScreenImage(::gnu::awt::xlib::XGraphicsConfiguration *, ::gnu::gcj::xlib::Drawable *, jint, jint, ::java::awt::image::ColorModel *);
  XOffScreenImage(::gnu::awt::xlib::XGraphicsConfiguration *, ::gnu::gcj::xlib::Drawable *, ::java::awt::image::ImageProducer *, ::java::awt::image::ColorModel *);
public:
  virtual ::gnu::gcj::xlib::Pixmap * getPixmap();
  virtual void flush();
  virtual ::java::awt::Graphics * getGraphics();
  virtual jint getHeight(::java::awt::image::ImageObserver *);
  virtual jint getHeight();
  virtual ::java::awt::image::ImageProducer * getSource();
  virtual jint getWidth(::java::awt::image::ImageObserver *);
  virtual jint getWidth();
  virtual ::java::lang::Object * getProperty(::java::lang::String *, ::java::awt::image::ImageObserver *);
  virtual ::java::awt::GraphicsConfiguration * getGraphicsConfiguration();
  virtual void imageComplete(jint);
  virtual void setColorModel(::java::awt::image::ColorModel *);
  virtual void setDimensions(jint, jint);
  virtual void setHints(jint);
  virtual void setPixels(jint, jint, jint, jint, ::java::awt::image::ColorModel *, JArray< jint > *, jint, jint);
  virtual void setPixels(jint, jint, jint, jint, ::java::awt::image::ColorModel *, JArray< jbyte > *, jint, jint);
  virtual void setProperties(::java::util::Hashtable *);
private:
  ::gnu::gcj::xlib::Pixmap * __attribute__((aligned(__alignof__( ::java::awt::Image)))) pixmap;
  ::gnu::awt::xlib::XGraphicsConfiguration * config;
  jint width;
  jint height;
  ::gnu::gcj::xlib::Drawable * drawable;
  ::java::awt::image::ImageProducer * prod;
  ::gnu::gcj::xlib::GC * gc;
  ::java::awt::image::ColorModel * pixmapColorModel;
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_awt_xlib_XOffScreenImage__
