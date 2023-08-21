from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class StudentRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.allusers.is_student:
            return redirect('access_denied')
        return super().dispatch(request, *args, **kwargs)


class LecturerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.allusers.is_lecturer(request.user):
            return redirect('access_denied')
        return super().dispatch(request, *args, **kwargs)


class AdmissionsTeamRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.allusers.is_admissions_team(request.user):
            return redirect('access_denied')
        return super().dispatch(request, *args, **kwargs)


class WebsiteAdminRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.allusers.is_website_admin(request.user):
            return redirect('access_denied')
        return super().dispatch(request, *args, **kwargs)
    

