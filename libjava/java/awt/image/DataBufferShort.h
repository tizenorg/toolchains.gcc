
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __java_awt_image_DataBufferShort__
#define __java_awt_image_DataBufferShort__

#pragma interface

#include <java/awt/image/DataBuffer.h>
#include <gcj/array.h>

extern "Java"
{
  namespace java
  {
    namespace awt
    {
      namespace image
      {
          class DataBufferShort;
      }
    }
  }
}

class java::awt::image::DataBufferShort : public ::java::awt::image::DataBuffer
{

public:
  DataBufferShort(jint);
  DataBufferShort(jint, jint);
  DataBufferShort(JArray< jshort > *, jint);
  DataBufferShort(JArray< jshort > *, jint, jint);
  DataBufferShort(JArray< JArray< jshort > * > *, jint);
  DataBufferShort(JArray< JArray< jshort > * > *, jint, JArray< jint > *);
  JArray< jshort > * getData();
  JArray< jshort > * getData(jint);
  JArray< JArray< jshort > * > * getBankData();
  jint getElem(jint);
  jint getElem(jint, jint);
  void setElem(jint, jint);
  void setElem(jint, jint, jint);
private:
  JArray< jshort > * __attribute__((aligned(__alignof__( ::java::awt::image::DataBuffer)))) data;
  JArray< JArray< jshort > * > * bankData;
public:
  static ::java::lang::Class class$;
};

#endif // __java_awt_image_DataBufferShort__
