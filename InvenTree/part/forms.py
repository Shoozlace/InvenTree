"""Django Forms for interacting with Part objects."""

from django import forms
from django.utils.translation import gettext_lazy as _

from common.forms import MatchItemForm
from InvenTree.fields import RoundingDecimalFormField
from InvenTree.forms import HelperForm
from InvenTree.helpers import clean_decimal

from .models import Part, PartInternalPriceBreak, PartSellPriceBreak


class PartImageDownloadForm(HelperForm):
    """Form for downloading an image from a URL."""

    url = forms.URLField(
        label=_('URL'),
        help_text=_('Image URL'),
        required=True,
    )

    class Meta:
        """Metaclass defines fields for this form"""
        model = Part
        fields = [
            'url',
        ]


class BomMatchItemForm(MatchItemForm):
    """Override MatchItemForm fields."""

    def get_special_field(self, col_guess, row, file_manager):
        """Set special fields."""
        # set quantity field
        if 'quantity' in col_guess.lower():
            return forms.CharField(
                required=False,
                widget=forms.NumberInput(attrs={
                    'name': 'quantity' + str(row['index']),
                    'class': 'numberinput',
                    'type': 'number',
                    'min': '0',
                    'step': 'any',
                    'value': clean_decimal(row.get('quantity', '')),
                })
            )

        return super().get_special_field(col_guess, row, file_manager)


class PartPriceForm(forms.Form):
    """Simple form for viewing part pricing information."""

    quantity = forms.IntegerField(
        required=True,
        initial=1,
        label=_('Quantity'),
        help_text=_('Input quantity for price calculation')
    )

    class Meta:
        """Metaclass defines fields for this form"""
        model = Part
        fields = [
            'quantity',
        ]


class EditPartSalePriceBreakForm(HelperForm):
    """Form for creating / editing a sale price for a part."""

    quantity = RoundingDecimalFormField(max_digits=10, decimal_places=5, label=_('Quantity'))

    class Meta:
        """Metaclass defines fields for this form"""
        model = PartSellPriceBreak
        fields = [
            'part',
            'quantity',
            'price',
        ]


class EditPartInternalPriceBreakForm(HelperForm):
    """Form for creating / editing a internal price for a part."""

    quantity = RoundingDecimalFormField(max_digits=10, decimal_places=5, label=_('Quantity'))

    class Meta:
        """Metaclass defines fields for this form"""
        model = PartInternalPriceBreak
        fields = [
            'part',
            'quantity',
            'price',
        ]
