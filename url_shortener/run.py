from app import create_app

if __name__ == '__main__':
    app = create_app()
    port = app.config['PORT']
    app.run(host='0.0.0.0', port=port)