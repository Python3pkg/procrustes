# (c) Svarga project under terms of the new BSD license


# Widgets
class Base(object):
    def __init__(self, data=None, prefix='form', id=None,
                 delimiter='__', error=None, **kwargs):
        self.marker = kwargs.pop('marker', False)
        self.data = data
        self.prefix = prefix
        self.id = id
        self.error = error
        self.label_name = kwargs.pop('label_name', None)
        if self.label_name is None:
            self.label_name = self.id
        self.parent = kwargs.get('parent', '')
        self.attrs = kwargs
        self.name = self.prefix + ('__' + id if id else '')
        self.parent_label = self.prefix + delimiter + self.parent


    def render(self):
        data = self.data if self.data else ''
        attrs = ' '.join('%s="%s"' % (name, attr) for name, attr
                                                    in self.attrs.items())
        if attrs:
            attrs += ' '
        return self.render_html(self.name, attrs, data)

    def render_html(self, name, attrs, data):
        return '<input id="{0}" name="{0}" {1}value="{2}">'.format(name, attrs,
                                                                         data)

    def label(self):
        name = self.prefix + '__' + self.id
        return '<label for="%s">%s</label>' % (name, self.label_name)


class Marker(Base):
    def render(self, *a, **kw):
        return ''

    def label(self, *a, **kw):
        return ''


class CheckBox(Base):
    def render_html(self, name, attrs, data):
        checked = ''
        if data:
            checked = ' checked'
        return ('<input type="checkbox" id="{0}" '
                'name="{0}" {1}value="True"{3}>').format(name, attrs,
                                                         data, checked)

class TextArea(Base):
    def render_html(self, name, attrs, data):
        return ('<textarea id="{0}" '
                'name="{0}" {1}>{2}</textarea>').format(name, attrs, data)


class HiddenInput(Base):
    def render_html(self, name, attrs, data):
        return ('<input type="password" id="{0}"'
                ' name="{0}" {1}value="{2}">').format(name, attrs, data)
