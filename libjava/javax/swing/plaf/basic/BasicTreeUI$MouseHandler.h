
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __javax_swing_plaf_basic_BasicTreeUI$MouseHandler__
#define __javax_swing_plaf_basic_BasicTreeUI$MouseHandler__

#pragma interface

#include <java/awt/event/MouseAdapter.h>
extern "Java"
{
  namespace java
  {
    namespace awt
    {
      namespace event
      {
          class MouseEvent;
      }
    }
  }
  namespace javax
  {
    namespace swing
    {
      namespace plaf
      {
        namespace basic
        {
            class BasicTreeUI;
            class BasicTreeUI$MouseHandler;
        }
      }
    }
  }
}

class javax::swing::plaf::basic::BasicTreeUI$MouseHandler : public ::java::awt::event::MouseAdapter
{

public:
  BasicTreeUI$MouseHandler(::javax::swing::plaf::basic::BasicTreeUI *);
  virtual void mousePressed(::java::awt::event::MouseEvent *);
  virtual void mouseDragged(::java::awt::event::MouseEvent *);
  virtual void mouseMoved(::java::awt::event::MouseEvent *);
  virtual void mouseReleased(::java::awt::event::MouseEvent *);
private:
  void handleEvent(::java::awt::event::MouseEvent *);
  jboolean __attribute__((aligned(__alignof__( ::java::awt::event::MouseAdapter)))) selectedOnPress;
public: // actually package-private
  ::javax::swing::plaf::basic::BasicTreeUI * this$0;
public:
  static ::java::lang::Class class$;
};

#endif // __javax_swing_plaf_basic_BasicTreeUI$MouseHandler__
