from behave import *


@when('Открыть логин форму')
def step_impl(context):
    context.investing_login_form = context.investing_main_page.open_login_form()


@then('Открылась логин форма')
def step_impl(context):
    assert context.investing_login_form.is_open_login_form() is True


@when('Проверка формы на пустые поля')
def step_impl(context):
    context.investing_login_form.submit()


@when('Проверяем форму при заполненном e-mail: "{login}"')
def step_impl(context, login):
    context.investing_login_form.input_login(login)
    context.investing_login_form.submit()


@when('Проверяем форму при заполненном e-mail и пароле "{password}"')
def step_impl(context, password):
    context.investing_login_form.input_password(password)
    context.investing_login_form.submit()


@then('Появилось предупреждение')
def step_impl(context):
    check_error = any((context.investing_login_form.is_email_error(),
                       context.investing_login_form.is_password_error(),
                       context.investing_login_form.is_authorization_error()))
    assert check_error is True
