import logging


class Logger:
  def __init__(self, name=None, level=logging.INFO, context=None):
    self.logger = logging.getLogger(name or __name__)
    self.level = level
    self.context = context or {}

  def __call__(self, msg, **extra):
    self.logger.log(
      level=self.level,
      msg=msg,
      extra={**self.context, **extra}
    )

  def info(self, msg, **extra):
    self.logger.info(
      msg=msg,
      extra={**self.context, **extra}
    )

  def debug(self, msg, **extra):
    self.logger.debug(
      msg=msg,
      extra={**self.context, **extra}
    )

  def warn(self, msg, **extra):
    self.logger.warn(
      msg=msg,
      extra={**self.context, **extra}
    )

  def warning(self, msg, **extra):
    self.logger.warning(
      msg=msg,
      extra={**self.context, **extra}
    )

  def exception(self, msg, **extra):
    self.logger.exception(
      msg=msg,
      extra={**self.context, **extra}
    )

  def error(self, msg, **extra):
    self.logger.error(
      msg=msg,
      extra={**self.context, **extra}
    )

  def critical(self, msg, **extra):
    self.logger.critical(
      msg=msg,
      extra={**self.context, **extra}
    )

  fatal = critical