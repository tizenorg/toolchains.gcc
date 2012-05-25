/* PR debug/43329 */
/* { dg-do run } */
/* { dg-options "-g" } */

static inline void
foo (int argx)
{
  int varx = argx;
  __asm__ volatile ("nop");			/* { dg-final { gdb-test 10 "argx" "25" } } */
  __asm__ volatile ("nop" : : "g" (varx));	/* { dg-final { gdb-test 10 "varx" "25" } } */
}

int i;

__attribute__((noinline))
void baz (int x)
{
  asm volatile ("" : : "r" (x) : "memory");
}

static inline void
bar (void)
{
  foo (25);
  i = i + 2;
  i = i * 2;
  i = i - 4;
  baz (i);
  i = i * 2;
  i = i >> 1;
  i = i << 6;
  baz (i);
  i = i + 2;
  i = i * 2;
  i = i - 4;
  baz (i);
  i = i * 2;
  i = i >> 6;
  i = i << 1;
  baz (i);
}

int
main (void)
{
  __asm__ volatile ("" : "=r" (i) : "0" (0));
  bar ();
  bar ();
  return i;
}
