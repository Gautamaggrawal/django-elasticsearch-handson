from django_elasticsearch_dsl import DocType, Index,fields
from .models import *
from django.contrib.auth.models import User
blog = Index('blog')

@blog.doc_type
class PostDocument(DocType):
	username = fields.ObjectField(properties={'username': fields.StringField()})
	class Meta:
		model = BlogPost
		related_models=[User]

		fields = [
		'posted_date',
		'title',
		'text',
		]
	def get_queryset(self):
		return super(PostDocument, self).get_queryset().select_related('username')

	def get_instances_from_related(self, related_instance):
		return related_instance.username_set.all()
		# if isinstance(related_instance, User):
		# 	return related_instance.blogpost
  #       # return tag_instance.car_set.all()




