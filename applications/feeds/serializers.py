# Standard Library
from typing import Dict, Union

# Rest Framework
from rest_framework import serializers

# Applications
from feeds.models import Entry, Location


class BulkEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["full_text", "channel", "is_resolved", "extra_parameters"]


class EntrySerializer(serializers.ModelSerializer):
    def create(self, validated_data: Dict[str, Union[str, bool]]):
        # Applications
        from feeds.tasks import process_entry

        instance: Entry = super().create(validated_data=validated_data)
        process_entry.apply_async(kwargs={"entry_id": instance.id})
        return instance

    class Meta:
        model = Entry
        fields = ["id", "full_text", "timestamp", "channel", "is_resolved", "extra_parameters"]


class LocationLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "loc"]


class LocationSerializer(serializers.ModelSerializer):
    raw = EntrySerializer(source="entry")

    class Meta:
        model = Location
        fields = ["id", "formatted_address", "loc", "viewport", "raw"]


class LocationFilterParamSerializer(serializers.Serializer):
    """
    Filter by query param: timestamp
    """

    timestamp__gte = serializers.DateTimeField(required=False)
    timestamp__lte = serializers.DateTimeField(required=False)
