/****************************************************************************
** Meta object code from reading C++ file 'qpad.h'
**
** Created by: The Qt Meta Object Compiler version 69 (Qt 6.9.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../qpad.h"
#include <QtGui/qtextcursor.h>
#include <QtCore/qmetatype.h>

#include <QtCore/qtmochelpers.h>

#include <memory>


#include <QtCore/qxptype_traits.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'qpad.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 69
#error "This file was generated using the moc from 6.9.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif

QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
QT_WARNING_DISABLE_GCC("-Wuseless-cast")
namespace {
struct qt_meta_tag_ZN4qpadE_t {};
} // unnamed namespace

template <> constexpr inline auto qpad::qt_create_metaobjectdata<qt_meta_tag_ZN4qpadE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "qpad",
        "on_pushButton_clicked",
        "",
        "on_pushButton_2_clicked",
        "on_pushButton_3_clicked",
        "on_pushButton_4_clicked",
        "on_spinBox_valueChanged",
        "value",
        "on_fontComboBox_currentFontChanged",
        "f",
        "on_comboBox_currentIndexChanged",
        "index",
        "nuevoDocumento",
        "nombre",
        "abrirArchivo",
        "guardarArchivo",
        "on_HTML_switch_clicked",
        "on_HTML_run_clicked",
        "on_actionPropiedades_triggered",
        "on_actionVersion_triggered",
        "updateFormatButtons",
        "toggleBold",
        "toggleItalic",
        "toggleUnderline",
        "toggleStrikeOut",
        "aumentarFuente",
        "disminuirFuente",
        "mostrarHtmlColoreado",
        "html",
        "exportarHTML2RTF",
        "htmlSemantico"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'on_pushButton_clicked'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'on_pushButton_2_clicked'
        QtMocHelpers::SlotData<void()>(3, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'on_pushButton_3_clicked'
        QtMocHelpers::SlotData<void()>(4, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'on_pushButton_4_clicked'
        QtMocHelpers::SlotData<void()>(5, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'on_spinBox_valueChanged'
        QtMocHelpers::SlotData<void(int)>(6, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { QMetaType::Int, 7 },
        }}),
        // Slot 'on_fontComboBox_currentFontChanged'
        QtMocHelpers::SlotData<void(const QFont &)>(8, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { QMetaType::QFont, 9 },
        }}),
        // Slot 'on_comboBox_currentIndexChanged'
        QtMocHelpers::SlotData<void(int)>(10, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { QMetaType::Int, 11 },
        }}),
        // Slot 'nuevoDocumento'
        QtMocHelpers::SlotData<void(const QString &)>(12, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { QMetaType::QString, 13 },
        }}),
        // Slot 'nuevoDocumento'
        QtMocHelpers::SlotData<void()>(12, 2, QMC::AccessPrivate | QMC::MethodCloned, QMetaType::Void),
        // Slot 'abrirArchivo'
        QtMocHelpers::SlotData<void()>(14, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'guardarArchivo'
        QtMocHelpers::SlotData<void()>(15, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'on_HTML_switch_clicked'
        QtMocHelpers::SlotData<void()>(16, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'on_HTML_run_clicked'
        QtMocHelpers::SlotData<void()>(17, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'on_actionPropiedades_triggered'
        QtMocHelpers::SlotData<void()>(18, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'on_actionVersion_triggered'
        QtMocHelpers::SlotData<void()>(19, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'updateFormatButtons'
        QtMocHelpers::SlotData<void()>(20, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'toggleBold'
        QtMocHelpers::SlotData<void()>(21, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'toggleItalic'
        QtMocHelpers::SlotData<void()>(22, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'toggleUnderline'
        QtMocHelpers::SlotData<void()>(23, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'toggleStrikeOut'
        QtMocHelpers::SlotData<void()>(24, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'aumentarFuente'
        QtMocHelpers::SlotData<void()>(25, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'disminuirFuente'
        QtMocHelpers::SlotData<void()>(26, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'mostrarHtmlColoreado'
        QtMocHelpers::SlotData<void(const QString &)>(27, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { QMetaType::QString, 28 },
        }}),
        // Slot 'exportarHTML2RTF'
        QtMocHelpers::SlotData<void()>(29, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'htmlSemantico'
        QtMocHelpers::SlotData<QString(const QString &)>(30, 2, QMC::AccessPrivate, QMetaType::QString, {{
            { QMetaType::QString, 28 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<qpad, qt_meta_tag_ZN4qpadE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject qpad::staticMetaObject = { {
    QMetaObject::SuperData::link<QMainWindow::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN4qpadE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN4qpadE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN4qpadE_t>.metaTypes,
    nullptr
} };

void qpad::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<qpad *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->on_pushButton_clicked(); break;
        case 1: _t->on_pushButton_2_clicked(); break;
        case 2: _t->on_pushButton_3_clicked(); break;
        case 3: _t->on_pushButton_4_clicked(); break;
        case 4: _t->on_spinBox_valueChanged((*reinterpret_cast< std::add_pointer_t<int>>(_a[1]))); break;
        case 5: _t->on_fontComboBox_currentFontChanged((*reinterpret_cast< std::add_pointer_t<QFont>>(_a[1]))); break;
        case 6: _t->on_comboBox_currentIndexChanged((*reinterpret_cast< std::add_pointer_t<int>>(_a[1]))); break;
        case 7: _t->nuevoDocumento((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 8: _t->nuevoDocumento(); break;
        case 9: _t->abrirArchivo(); break;
        case 10: _t->guardarArchivo(); break;
        case 11: _t->on_HTML_switch_clicked(); break;
        case 12: _t->on_HTML_run_clicked(); break;
        case 13: _t->on_actionPropiedades_triggered(); break;
        case 14: _t->on_actionVersion_triggered(); break;
        case 15: _t->updateFormatButtons(); break;
        case 16: _t->toggleBold(); break;
        case 17: _t->toggleItalic(); break;
        case 18: _t->toggleUnderline(); break;
        case 19: _t->toggleStrikeOut(); break;
        case 20: _t->aumentarFuente(); break;
        case 21: _t->disminuirFuente(); break;
        case 22: _t->mostrarHtmlColoreado((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 23: _t->exportarHTML2RTF(); break;
        case 24: { QString _r = _t->htmlSemantico((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1])));
            if (_a[0]) *reinterpret_cast< QString*>(_a[0]) = std::move(_r); }  break;
        default: ;
        }
    }
}

const QMetaObject *qpad::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *qpad::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN4qpadE_t>.strings))
        return static_cast<void*>(this);
    return QMainWindow::qt_metacast(_clname);
}

int qpad::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 25)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 25;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 25)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 25;
    }
    return _id;
}
QT_WARNING_POP
