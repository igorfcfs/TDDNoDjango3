from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'D:\OneDrive\IGOR\Cursos\Alura\04.FormacaoDjango\04.ValidacaoDeFormulariosEDeploy\02.TDDNoDjango3DesenvolvimentoGuiadoPorTestes\Projeto\TDDBuscaAnimal\geckodriver.exe')

    def tearDown(self):
        self.browser.quit()

    # def test_para_verificar_se_a_janela_do_browser_esta_ok(self):
    #     self.browser.get('https://alura.com.br')

    def test_abre_janela_do_firefox(self):
        self.browser.get(self.live_server_url)

    def test_deu_ruim(self):
        """Teste de exemplo de erro"""
        self.fail('Teste falhou - deu ruim mesmo')
