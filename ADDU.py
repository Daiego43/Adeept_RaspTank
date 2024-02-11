
"""
A Dumb Docker User. (ADDU)
"""
import os

def delete_all_images():
    """
    Delete all images.
    """
    os.system("docker rmi $(docker images -q)")

if __name__ == '__main__':
    delete_all_images()