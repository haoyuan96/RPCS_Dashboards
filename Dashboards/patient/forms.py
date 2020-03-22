from django import forms


class SurveyForm(forms.Form):
    falls = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'falls', 'class': 'custom-control-input'}))

    depression = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'depression', 'class': 'custom-control-input'}))

    dyskinesia = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'id_user_type', 'class': 'custom-control-input'}))

    movement = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
            choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'movement', 'class': 'custom-control-input'}))

    thinking = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'thinking', 'class': 'custom-control-input'}))
    walking = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'walking', 'class': 'custom-control-input'}))

    chest_pain = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'chest_pain', 'class': 'custom-control-input'}))

    tremor = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'tremor', 'class': 'custom-control-input'}))