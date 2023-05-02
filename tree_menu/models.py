from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=128, null=False, unique=True)
    left = models.IntegerField(blank=True, null=True)
    right = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey(to='self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    level = models.IntegerField(blank=True, null=True)
    url = models.CharField(default='menu/', max_length=128)
    root = models.ForeignKey(to='self', blank=True, null=True, related_name='head', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
    
    def save(self, *args, **kwargs):
        super(Menu, self).save(*args, **kwargs)
        self.set_menu_tree()

    def set_menu_tree(self, left=1, parent=None, level=1, root=None):
        for i in type(self).objects.filter(parent=parent):
            if i.parent is None:
                root = i
            obj, children_count = i, 0
            while obj.children.exists():
                for child in obj.children.all():
                    children_count += 1
                    obj = child
            data = {
                'level': level,
                'left': left,
                'right': left + (children_count * 2) + 1,
                'root': root
            }
            type(self).objects.filter(id=i.id).update(**data)
            left = data['right'] + 1
            self.set_menu_tree(left=data['left'] + 1, parent=i.id, level=data['level'] + 1, root=root)

    def __str__(self):
        return self.name
    
    def view_root(self):
        return str(self.root)

    def view_children(self):
        return '\n'.join(child.name for child in self.children.all())

    def view_parent(self):
        return '\n'.join(item.name for item in Menu.objects.all())

    