# Make sure we have the correct relative path
from sys import path, exc_info, stdout
path.insert(0, '..')  # chang to the root directory of the project
#########################################################################
from zeppos_logging.app_logger import AppLogger
from zeppos_logging.app_logger_json_conifg_name import AppLoggerJsonConfigName


def main():
    AppLogger.logger.info(f"Start test_bash_operator_failure")
    AppLogger.logger.info(f"End test_bash_operator_failure")


if __name__ == '__main__':
    AppLogger.configure_and_get_logger(
        'salesforce',
        AppLoggerJsonConfigName.default_with_watchtower_format_1(),
        watchtower_log_group="airflow",
        watchtower_stream_name="test_bash_operator_failure"
    )
    main()
