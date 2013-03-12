
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __javax_swing_JTable__
#define __javax_swing_JTable__

#pragma interface

#include <javax/swing/JComponent.h>
#include <gcj/array.h>

extern "Java"
{
  namespace java
  {
    namespace awt
    {
        class Color;
        class Component;
        class Dimension;
        class Point;
        class Rectangle;
    }
  }
  namespace javax
  {
    namespace accessibility
    {
        class AccessibleContext;
    }
    namespace swing
    {
        class JScrollPane;
        class JTable;
        class JTable$TableColumnPropertyChangeHandler;
        class ListSelectionModel;
        class SizeSequence;
      namespace event
      {
          class ChangeEvent;
          class ListSelectionEvent;
          class TableColumnModelEvent;
          class TableModelEvent;
      }
      namespace plaf
      {
          class TableUI;
      }
      namespace table
      {
          class JTableHeader;
          class TableCellEditor;
          class TableCellRenderer;
          class TableColumn;
          class TableColumnModel;
          class TableModel;
      }
    }
  }
}

class javax::swing::JTable : public ::javax::swing::JComponent
{

public:
  JTable();
  JTable(jint, jint);
  JTable(JArray< JArray< ::java::lang::Object * > * > *, JArray< ::java::lang::Object * > *);
  JTable(::javax::swing::table::TableModel *);
  JTable(::javax::swing::table::TableModel *, ::javax::swing::table::TableColumnModel *);
  JTable(::javax::swing::table::TableModel *, ::javax::swing::table::TableColumnModel *, ::javax::swing::ListSelectionModel *);
  JTable(::java::util::Vector *, ::java::util::Vector *);
public: // actually protected
  virtual void initializeLocalVars();
public:
  virtual void addColumn(::javax::swing::table::TableColumn *);
public: // actually protected
  virtual void createDefaultEditors();
  virtual void createDefaultRenderers();
public:
  static ::javax::swing::JScrollPane * createScrollPaneForTable(::javax::swing::JTable *);
public: // actually protected
  virtual ::javax::swing::table::TableColumnModel * createDefaultColumnModel();
  virtual ::javax::swing::table::TableModel * createDefaultDataModel();
  virtual ::javax::swing::ListSelectionModel * createDefaultSelectionModel();
  virtual ::javax::swing::table::JTableHeader * createDefaultTableHeader();
public:
  virtual void columnAdded(::javax::swing::event::TableColumnModelEvent *);
  virtual void columnMarginChanged(::javax::swing::event::ChangeEvent *);
  virtual void columnMoved(::javax::swing::event::TableColumnModelEvent *);
  virtual void columnRemoved(::javax::swing::event::TableColumnModelEvent *);
  virtual void columnSelectionChanged(::javax::swing::event::ListSelectionEvent *);
  virtual void editingCanceled(::javax::swing::event::ChangeEvent *);
  virtual void editingStopped(::javax::swing::event::ChangeEvent *);
  virtual void tableChanged(::javax::swing::event::TableModelEvent *);
private:
  void handleCompleteChange(::javax::swing::event::TableModelEvent *);
  void handleInsert(::javax::swing::event::TableModelEvent *);
  void handleDelete(::javax::swing::event::TableModelEvent *);
  void handleUpdate(::javax::swing::event::TableModelEvent *);
  void checkSelection();
public:
  virtual void valueChanged(::javax::swing::event::ListSelectionEvent *);
  virtual jint columnAtPoint(::java::awt::Point *);
  virtual jint rowAtPoint(::java::awt::Point *);
  virtual ::java::awt::Rectangle * getCellRect(jint, jint, jboolean);
  virtual void clearSelection();
  virtual jint getSelectedRow();
  virtual ::javax::swing::ListSelectionModel * getSelectionModel();
  virtual jint getScrollableBlockIncrement(::java::awt::Rectangle *, jint, jint);
  virtual jboolean getScrollableTracksViewportHeight();
  virtual jboolean getScrollableTracksViewportWidth();
  virtual jint getScrollableUnitIncrement(::java::awt::Rectangle *, jint, jint);
  virtual ::javax::swing::table::TableCellEditor * getCellEditor(jint, jint);
  virtual ::javax::swing::table::TableCellEditor * getDefaultEditor(::java::lang::Class *);
  virtual ::javax::swing::table::TableCellRenderer * getCellRenderer(jint, jint);
  virtual void setDefaultRenderer(::java::lang::Class *, ::javax::swing::table::TableCellRenderer *);
  virtual ::javax::swing::table::TableCellRenderer * getDefaultRenderer(::java::lang::Class *);
  virtual jint convertColumnIndexToModel(jint);
  virtual jint convertColumnIndexToView(jint);
  virtual ::java::awt::Component * prepareRenderer(::javax::swing::table::TableCellRenderer *, jint, jint);
  virtual jboolean getAutoCreateColumnsFromModel();
  virtual jint getAutoResizeMode();
  virtual jint getRowHeight();
  virtual jint getRowHeight(jint);
  virtual jint getRowMargin();
  virtual jboolean getRowSelectionAllowed();
  virtual jboolean getCellSelectionEnabled();
  virtual ::javax::swing::table::TableModel * getModel();
  virtual jint getColumnCount();
  virtual jint getRowCount();
  virtual ::javax::swing::table::TableColumnModel * getColumnModel();
  virtual jint getSelectedColumn();
private:
  static jint countSelections(::javax::swing::ListSelectionModel *);
  static JArray< jint > * getSelections(::javax::swing::ListSelectionModel *);
public:
  virtual jint getSelectedColumnCount();
  virtual JArray< jint > * getSelectedColumns();
  virtual jboolean getColumnSelectionAllowed();
  virtual jint getSelectedRowCount();
  virtual JArray< jint > * getSelectedRows();
  virtual ::javax::accessibility::AccessibleContext * getAccessibleContext();
  virtual ::javax::swing::table::TableCellEditor * getCellEditor();
  virtual jboolean getDragEnabled();
  virtual ::java::awt::Color * getGridColor();
  virtual ::java::awt::Dimension * getIntercellSpacing();
  virtual ::java::awt::Dimension * getPreferredScrollableViewportSize();
  virtual ::java::awt::Color * getSelectionBackground();
  virtual ::java::awt::Color * getSelectionForeground();
  virtual jboolean getShowHorizontalLines();
  virtual jboolean getShowVerticalLines();
  virtual ::javax::swing::table::JTableHeader * getTableHeader();
  virtual void removeColumn(::javax::swing::table::TableColumn *);
  virtual void moveColumn(jint, jint);
  virtual void setAutoCreateColumnsFromModel(jboolean);
  virtual void setAutoResizeMode(jint);
  virtual void setRowHeight(jint);
  virtual void setRowHeight(jint, jint);
  virtual void setRowMargin(jint);
  virtual void setRowSelectionAllowed(jboolean);
  virtual void setCellSelectionEnabled(jboolean);
  virtual void setModel(::javax::swing::table::TableModel *);
  virtual void setColumnModel(::javax::swing::table::TableColumnModel *);
  virtual void setColumnSelectionAllowed(jboolean);
  virtual void setSelectionModel(::javax::swing::ListSelectionModel *);
  virtual void setSelectionMode(jint);
  virtual void setCellEditor(::javax::swing::table::TableCellEditor *);
  virtual void setDragEnabled(jboolean);
  virtual void setGridColor(::java::awt::Color *);
  virtual void setIntercellSpacing(::java::awt::Dimension *);
  virtual void setPreferredScrollableViewportSize(::java::awt::Dimension *);
  virtual void setSelectionBackground(::java::awt::Color *);
  virtual void setSelectionForeground(::java::awt::Color *);
  virtual void setShowGrid(jboolean);
  virtual void setShowHorizontalLines(jboolean);
  virtual void setShowVerticalLines(jboolean);
  virtual void setTableHeader(::javax::swing::table::JTableHeader *);
public: // actually protected
  virtual void configureEnclosingScrollPane();
  virtual void unconfigureEnclosingScrollPane();
public:
  virtual void addNotify();
  virtual void removeNotify();
private:
  void distributeSpill(JArray< ::javax::swing::table::TableColumn * > *, jint);
  void distributeSpillResizing(JArray< ::javax::swing::table::TableColumn * > *, jint, ::javax::swing::table::TableColumn *);
public:
  virtual void doLayout();
public: // actually package-private
  virtual jint getLeftResizingBoundary();
public:
  virtual void sizeColumnsToFit(jboolean);
  virtual void sizeColumnsToFit(jint);
  virtual ::java::lang::String * getUIClassID();
  virtual ::javax::swing::plaf::TableUI * getUI();
  virtual void setUI(::javax::swing::plaf::TableUI *);
  virtual void updateUI();
  virtual ::java::lang::Class * getColumnClass(jint);
  virtual ::java::lang::String * getColumnName(jint);
  virtual jint getEditingColumn();
  virtual void setEditingColumn(jint);
  virtual jint getEditingRow();
  virtual void setEditingRow(jint);
  virtual ::java::awt::Component * getEditorComponent();
  virtual jboolean isEditing();
  virtual void setDefaultEditor(::java::lang::Class *, ::javax::swing::table::TableCellEditor *);
  virtual void addColumnSelectionInterval(jint, jint);
  virtual void addRowSelectionInterval(jint, jint);
  virtual void setColumnSelectionInterval(jint, jint);
  virtual void setRowSelectionInterval(jint, jint);
  virtual void removeColumnSelectionInterval(jint, jint);
  virtual void removeRowSelectionInterval(jint, jint);
  virtual jboolean isColumnSelected(jint);
  virtual jboolean isRowSelected(jint);
  virtual jboolean isCellSelected(jint, jint);
  virtual void selectAll();
  virtual ::java::lang::Object * getValueAt(jint, jint);
  virtual void setValueAt(::java::lang::Object *, jint, jint);
  virtual ::javax::swing::table::TableColumn * getColumn(::java::lang::Object *);
  virtual jboolean isCellEditable(jint, jint);
  virtual void createDefaultColumnsFromModel();
  virtual void changeSelection(jint, jint, jboolean, jboolean);
  virtual jboolean editCellAt(jint, jint);
private:
  void moveToCellBeingEdited(::java::awt::Component *);
public:
  virtual jboolean editCellAt(jint, jint, ::java::util::EventObject *);
  virtual void removeEditor();
  virtual ::java::awt::Component * prepareEditor(::javax::swing::table::TableCellEditor *, jint, jint);
public: // actually protected
  virtual void resizeAndRepaint();
public:
  virtual void setSurrendersFocusOnKeystroke(jboolean);
  virtual jboolean getSurrendersFocusOnKeystroke();
public: // actually package-private
  virtual void setUIProperty(::java::lang::String *, ::java::lang::Object *);
private:
  static const jlong serialVersionUID = 3876025080382781659LL;
public: // actually package-private
  ::javax::swing::JTable * __attribute__((aligned(__alignof__( ::javax::swing::JComponent)))) this_table;
public:
  static const jint AUTO_RESIZE_OFF = 0;
  static const jint AUTO_RESIZE_NEXT_COLUMN = 1;
  static const jint AUTO_RESIZE_SUBSEQUENT_COLUMNS = 2;
  static const jint AUTO_RESIZE_ALL_COLUMNS = 4;
  static const jint AUTO_RESIZE_LAST_COLUMN = 3;
public: // actually protected
  ::java::util::Hashtable * defaultEditorsByColumnClass;
  ::java::util::Hashtable * defaultRenderersByColumnClass;
  jint editingColumn;
  jint editingRow;
  ::java::awt::Component * editorComp;
  jboolean autoCreateColumnsFromModel;
  jint autoResizeMode;
  jint rowHeight;
  jint rowMargin;
  jboolean rowSelectionAllowed;
  jboolean cellSelectionEnabled;
  ::javax::swing::table::TableModel * dataModel;
  ::javax::swing::table::TableColumnModel * columnModel;
  ::javax::swing::ListSelectionModel * selectionModel;
  ::javax::swing::table::TableCellEditor * cellEditor;
private:
  jboolean dragEnabled;
public: // actually protected
  ::java::awt::Color * gridColor;
  ::java::awt::Dimension * preferredViewportSize;
  ::java::awt::Color * selectionBackground;
private:
  static ::java::lang::String * SELECTION_BACKGROUND_CHANGED_PROPERTY;
public: // actually protected
  ::java::awt::Color * selectionForeground;
private:
  static ::java::lang::String * SELECTION_FOREGROUND_CHANGED_PROPERTY;
public: // actually protected
  jboolean showHorizontalLines;
  jboolean showVerticalLines;
  ::javax::swing::table::JTableHeader * tableHeader;
public: // actually package-private
  ::javax::swing::JTable$TableColumnPropertyChangeHandler * tableColumnPropertyChangeHandler;
private:
  jboolean surrendersFocusOnKeystroke;
  ::java::awt::Rectangle * rectCache;
  jboolean clientRowHeightSet;
  ::javax::swing::SizeSequence * rowHeights;
  ::javax::swing::table::TableCellEditor * booleanInvertingEditor;
public: // actually package-private
  static jboolean $assertionsDisabled;
public:
  static ::java::lang::Class class$;
};

#endif // __javax_swing_JTable__
