from distutils.core import setup
setup(
  name = 'easypromtparse',
  packages = ['easypromtparse'],
  version = '0.1',
  license='MIT',
  description = 'This tool allows you to parse any command from a string or prompt to separate entities',
  author = 'Nikita_Ton',
  author_email = 'nikita00ton@gmail.ru',
  url = 'https://github.com/Cwinka/EasyPromtParse',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['promt', 'parse'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)