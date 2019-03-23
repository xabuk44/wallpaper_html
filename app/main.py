from flask import Flask, render_template, request

from app import wallpaper


def main():
    app = Flask(__name__)

    @app.route('/')
    def index():
        wall_length = request.args.get('wall_length')
        wall_width = request.args.get('wall_width')
        wall_height = request.args.get('wall_height')
        wallpaper_width = request.args.get('wallpaper_width')
        wallpaper_length = request.args.get('wallpaper_length')
        if wallpaper_length and wall_width and wall_height and wallpaper_length and wallpaper_width:
            result = wallpaper(float(wall_length), float(wall_width), float(wall_height), float(wallpaper_width), float(wallpaper_length))
            return render_template('index.html', title='result', result=result, wall_length=wall_length, wall_width=wall_width, wall_height=wall_height, wallpaper_width=wallpaper_width, wallpaper_length=wallpaper_length)

        return render_template('index.html', title='result',)

    app.run(port=9001, debug=True)


if __name__ == '__main__':
    main()
