# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtPdf, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtPdf`

import PySide6.QtPdf
import PySide6.QtCore
import PySide6.QtGui

import enum
from typing import ClassVar, Dict, List, Union, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


NoneType = type(None)


class QIntList(object): ...


class QPdfBookmarkModel(PySide6.QtCore.QAbstractItemModel):

    documentChanged          : ClassVar[Signal] = ... # documentChanged(QPdfDocument*)

    class Role(enum.IntEnum):

        Title                    : QPdfBookmarkModel.Role = ... # 0x100
        Level                    : QPdfBookmarkModel.Role = ... # 0x101
        Page                     : QPdfBookmarkModel.Role = ... # 0x102
        Location                 : QPdfBookmarkModel.Role = ... # 0x103
        Zoom                     : QPdfBookmarkModel.Role = ... # 0x104
        NRoles                   : QPdfBookmarkModel.Role = ... # 0x105


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int: ...
    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int) -> Any: ...
    def document(self) -> PySide6.QtPdf.QPdfDocument: ...
    def index(self, row: int, column: int, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> PySide6.QtCore.QModelIndex: ...
    @overload
    def parent(self) -> PySide6.QtCore.QObject: ...
    @overload
    def parent(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtCore.QModelIndex: ...
    def roleNames(self) -> Dict[int, PySide6.QtCore.QByteArray]: ...
    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int: ...
    def setDocument(self, document: PySide6.QtPdf.QPdfDocument) -> None: ...


class QPdfDocument(PySide6.QtCore.QObject):

    pageCountChanged         : ClassVar[Signal] = ... # pageCountChanged(int)
    pageModelChanged         : ClassVar[Signal] = ... # pageModelChanged()
    passwordChanged          : ClassVar[Signal] = ... # passwordChanged()
    passwordRequired         : ClassVar[Signal] = ... # passwordRequired()
    statusChanged            : ClassVar[Signal] = ... # statusChanged(QPdfDocument::Status)

    class Error(enum.Enum):

        None_                    : QPdfDocument.Error = ... # 0x0
        Unknown                  : QPdfDocument.Error = ... # 0x1
        DataNotYetAvailable      : QPdfDocument.Error = ... # 0x2
        FileNotFound             : QPdfDocument.Error = ... # 0x3
        InvalidFileFormat        : QPdfDocument.Error = ... # 0x4
        IncorrectPassword        : QPdfDocument.Error = ... # 0x5
        UnsupportedSecurityScheme: QPdfDocument.Error = ... # 0x6


    class MetaDataField(enum.Enum):

        Title                    : QPdfDocument.MetaDataField = ... # 0x0
        Subject                  : QPdfDocument.MetaDataField = ... # 0x1
        Author                   : QPdfDocument.MetaDataField = ... # 0x2
        Keywords                 : QPdfDocument.MetaDataField = ... # 0x3
        Producer                 : QPdfDocument.MetaDataField = ... # 0x4
        Creator                  : QPdfDocument.MetaDataField = ... # 0x5
        CreationDate             : QPdfDocument.MetaDataField = ... # 0x6
        ModificationDate         : QPdfDocument.MetaDataField = ... # 0x7


    class PageModelRole(enum.Enum):

        Label                    : QPdfDocument.PageModelRole = ... # 0x100
        PointSize                : QPdfDocument.PageModelRole = ... # 0x101
        NRoles                   : QPdfDocument.PageModelRole = ... # 0x102


    class Status(enum.Enum):

        Null                     : QPdfDocument.Status = ... # 0x0
        Loading                  : QPdfDocument.Status = ... # 0x1
        Ready                    : QPdfDocument.Status = ... # 0x2
        Unloading                : QPdfDocument.Status = ... # 0x3
        Error                    : QPdfDocument.Status = ... # 0x4


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def close(self) -> None: ...
    def error(self) -> PySide6.QtPdf.QPdfDocument.Error: ...
    def getAllText(self, page: int) -> PySide6.QtPdf.QPdfSelection: ...
    def getSelection(self, page: int, start: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element], end: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> PySide6.QtPdf.QPdfSelection: ...
    def getSelectionAtIndex(self, page: int, startIndex: int, maxLength: int) -> PySide6.QtPdf.QPdfSelection: ...
    @overload
    def load(self, device: PySide6.QtCore.QIODevice) -> None: ...
    @overload
    def load(self, fileName: str) -> PySide6.QtPdf.QPdfDocument.Error: ...
    def metaData(self, field: PySide6.QtPdf.QPdfDocument.MetaDataField) -> Any: ...
    def pageCount(self) -> int: ...
    def pageLabel(self, page: int) -> str: ...
    def pageModel(self) -> PySide6.QtCore.QAbstractListModel: ...
    def pagePointSize(self, page: int) -> PySide6.QtCore.QSizeF: ...
    def password(self) -> str: ...
    def render(self, page: int, imageSize: PySide6.QtCore.QSize, options: PySide6.QtPdf.QPdfDocumentRenderOptions = ...) -> PySide6.QtGui.QImage: ...
    def setPassword(self, password: str) -> None: ...
    def status(self) -> PySide6.QtPdf.QPdfDocument.Status: ...


class QPdfDocumentRenderOptions(Shiboken.Object):

    class RenderFlag(enum.Flag):

        None_                    : QPdfDocumentRenderOptions.RenderFlag = ... # 0x0
        Annotations              : QPdfDocumentRenderOptions.RenderFlag = ... # 0x1
        OptimizedForLcd          : QPdfDocumentRenderOptions.RenderFlag = ... # 0x2
        Grayscale                : QPdfDocumentRenderOptions.RenderFlag = ... # 0x4
        ForceHalftone            : QPdfDocumentRenderOptions.RenderFlag = ... # 0x8
        TextAliased              : QPdfDocumentRenderOptions.RenderFlag = ... # 0x10
        ImageAliased             : QPdfDocumentRenderOptions.RenderFlag = ... # 0x20
        PathAliased              : QPdfDocumentRenderOptions.RenderFlag = ... # 0x40


    class Rotation(enum.Enum):

        None_                    : QPdfDocumentRenderOptions.Rotation = ... # 0x0
        Clockwise90              : QPdfDocumentRenderOptions.Rotation = ... # 0x1
        Clockwise180             : QPdfDocumentRenderOptions.Rotation = ... # 0x2
        Clockwise270             : QPdfDocumentRenderOptions.Rotation = ... # 0x3


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QPdfDocumentRenderOptions: PySide6.QtPdf.QPdfDocumentRenderOptions) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def renderFlags(self) -> PySide6.QtPdf.QPdfDocumentRenderOptions.RenderFlag: ...
    def rotation(self) -> PySide6.QtPdf.QPdfDocumentRenderOptions.Rotation: ...
    def scaledClipRect(self) -> PySide6.QtCore.QRect: ...
    def scaledSize(self) -> PySide6.QtCore.QSize: ...
    def setRenderFlags(self, r: PySide6.QtPdf.QPdfDocumentRenderOptions.RenderFlag) -> None: ...
    def setRotation(self, r: PySide6.QtPdf.QPdfDocumentRenderOptions.Rotation) -> None: ...
    def setScaledClipRect(self, r: PySide6.QtCore.QRect) -> None: ...
    def setScaledSize(self, s: PySide6.QtCore.QSize) -> None: ...


class QPdfLink(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPdf.QPdfLink) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def contextAfter(self) -> str: ...
    def contextBefore(self) -> str: ...
    def copyToClipboard(self, mode: PySide6.QtGui.QClipboard.Mode = ...) -> None: ...
    def isValid(self) -> bool: ...
    def location(self) -> PySide6.QtCore.QPointF: ...
    def page(self) -> int: ...
    def rectangles(self) -> List[PySide6.QtCore.QRectF]: ...
    def swap(self, other: PySide6.QtPdf.QPdfLink) -> None: ...
    def toString(self) -> str: ...
    def url(self) -> PySide6.QtCore.QUrl: ...
    def zoom(self) -> float: ...


class QPdfPageNavigator(PySide6.QtCore.QObject):

    backAvailableChanged     : ClassVar[Signal] = ... # backAvailableChanged(bool)
    currentLocationChanged   : ClassVar[Signal] = ... # currentLocationChanged(QPointF)
    currentPageChanged       : ClassVar[Signal] = ... # currentPageChanged(int)
    currentZoomChanged       : ClassVar[Signal] = ... # currentZoomChanged(double)
    forwardAvailableChanged  : ClassVar[Signal] = ... # forwardAvailableChanged(bool)
    jumped                   : ClassVar[Signal] = ... # jumped(QPdfLink)

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def back(self) -> None: ...
    def backAvailable(self) -> bool: ...
    def clear(self) -> None: ...
    def currentLink(self) -> PySide6.QtPdf.QPdfLink: ...
    def currentLocation(self) -> PySide6.QtCore.QPointF: ...
    def currentPage(self) -> int: ...
    def currentZoom(self) -> float: ...
    def forward(self) -> None: ...
    def forwardAvailable(self) -> bool: ...
    @overload
    def jump(self, destination: PySide6.QtPdf.QPdfLink) -> None: ...
    @overload
    def jump(self, page: int, location: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element], zoom: float = ...) -> None: ...
    def update(self, page: int, location: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element], zoom: float) -> None: ...


class QPdfPageRenderer(PySide6.QtCore.QObject):

    documentChanged          : ClassVar[Signal] = ... # documentChanged(QPdfDocument*)
    pageRendered             : ClassVar[Signal] = ... # pageRendered(int,QSize,QImage,QPdfDocumentRenderOptions,qulonglong)
    renderModeChanged        : ClassVar[Signal] = ... # renderModeChanged(QPdfPageRenderer::RenderMode)

    class RenderMode(enum.Enum):

        MultiThreaded            : QPdfPageRenderer.RenderMode = ... # 0x0
        SingleThreaded           : QPdfPageRenderer.RenderMode = ... # 0x1


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def document(self) -> PySide6.QtPdf.QPdfDocument: ...
    def renderMode(self) -> PySide6.QtPdf.QPdfPageRenderer.RenderMode: ...
    def requestPage(self, pageNumber: int, imageSize: PySide6.QtCore.QSize, options: PySide6.QtPdf.QPdfDocumentRenderOptions = ...) -> int: ...
    def setDocument(self, document: PySide6.QtPdf.QPdfDocument) -> None: ...
    def setRenderMode(self, mode: PySide6.QtPdf.QPdfPageRenderer.RenderMode) -> None: ...


class QPdfSearchModel(PySide6.QtCore.QAbstractListModel):

    documentChanged          : ClassVar[Signal] = ... # documentChanged()
    searchStringChanged      : ClassVar[Signal] = ... # searchStringChanged()

    class Role(enum.Enum):

        Page                     : QPdfSearchModel.Role = ... # 0x100
        IndexOnPage              : QPdfSearchModel.Role = ... # 0x101
        Location                 : QPdfSearchModel.Role = ... # 0x102
        ContextBefore            : QPdfSearchModel.Role = ... # 0x103
        ContextAfter             : QPdfSearchModel.Role = ... # 0x104
        NRoles                   : QPdfSearchModel.Role = ... # 0x105


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int) -> Any: ...
    def document(self) -> PySide6.QtPdf.QPdfDocument: ...
    def onDocumentPageCountChanged(self, count: int) -> None: ...
    def resultAtIndex(self, index: int) -> PySide6.QtPdf.QPdfLink: ...
    def resultsOnPage(self, page: int) -> List[PySide6.QtPdf.QPdfLink]: ...
    def roleNames(self) -> Dict[int, PySide6.QtCore.QByteArray]: ...
    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> int: ...
    def searchString(self) -> str: ...
    def setDocument(self, document: PySide6.QtPdf.QPdfDocument) -> None: ...
    def setSearchString(self, searchString: str) -> None: ...
    def timerEvent(self, event: PySide6.QtCore.QTimerEvent) -> None: ...
    def updatePage(self, page: int) -> None: ...


class QPdfSelection(Shiboken.Object):

    def __init__(self, other: PySide6.QtPdf.QPdfSelection) -> None: ...

    def boundingRectangle(self) -> PySide6.QtCore.QRectF: ...
    def bounds(self) -> List[PySide6.QtGui.QPolygonF]: ...
    def copyToClipboard(self, mode: PySide6.QtGui.QClipboard.Mode = ...) -> None: ...
    def endIndex(self) -> int: ...
    def isValid(self) -> bool: ...
    def startIndex(self) -> int: ...
    def swap(self, other: PySide6.QtPdf.QPdfSelection) -> None: ...
    def text(self) -> str: ...


# eof
