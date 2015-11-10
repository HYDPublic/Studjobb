# -*- coding: utf-8 -*-
from application import app
from controllers import * 

app.error_handlers[500] = error_controller.exception 
app.error_handlers[404] = error_controller.not_found 
app.add_url_rule('/sitemap.xml', view_func = robot_controller.sitemap)
app.add_url_rule('/robots.txt', view_func = robot_controller.robots)

# Board
app.add_url_rule('/', 'board.view', view_func = board_controller.view)
app.add_url_rule('/om', 'board.about', view_func = board_controller.about)
app.add_url_rule('/admin', 'board.control_panel', view_func = board_controller.control_panel)

# Job
app.add_url_rule('/stilling/<int:id>/', 'job.view', view_func = job_controller.view)
app.add_url_rule('/stilling/<int:id>/<string:token>', 'job.preview', view_func = job_controller.preview)
app.add_url_rule('/admin/stilling/', 'job.new', view_func = job_controller.new)
app.add_url_rule('/admin/stilling/<int:id>/', 'job.edit', view_func = job_controller.edit)
app.add_url_rule('/admin/stilling/', 'job.create', view_func = job_controller.create, methods = ['POST'])
app.add_url_rule('/admin/stilling/<int:id>/', 'job.update', view_func = job_controller.update, methods = ['POST'])

# Scraped job
app.add_url_rule('/admin/skrapt/<string:guid>/', 'scraped_job.edit', view_func = scraped_job_controller.edit)
app.add_url_rule('/admin/skrapt/<string:guid>/delete', 'scraped_job.delete', view_func = scraped_job_controller.delete, methods = ['GET'])

# Company
app.add_url_rule('/admin/selskap/', 'comapany.new', view_func = company_controller.new)
app.add_url_rule('/admin/selskap/list', 'company.list', view_func = company_controller.list)
app.add_url_rule('/admin/selskap/<int:id>/', 'company.edit', view_func = company_controller.edit)
app.add_url_rule('/admin/selskap/', 'company.create', view_func = company_controller.create, methods = ['POST'])
app.add_url_rule('/admin/selskap/<int:id>/', 'company.update', view_func = company_controller.update, methods = ['POST'])

# Mail
app.add_url_rule('/admin/stilling/<int:id>/mail', 'mail.new', view_func = mailer_controller.new)
app.add_url_rule('/admin/stilling/<int:id>/mail', 'mail.create', view_func = mailer_controller.create, methods = ['POST'])

# Crawler
app.add_url_rule('/admin/crawl/', 'crawler.crawl', view_func = crawler_controller.crawl)
