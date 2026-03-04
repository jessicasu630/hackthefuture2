const navBarLinks: { name: string; url: string }[] = [];

const footerLinks = [
  {
    section: 'Plateforme',
    links: [
      { name: 'Resolv DRS', url: '/fr' },
      { name: 'Architecture', url: '#architecture' },
      { name: "Cas d'usage", url: '#use-cases' },
    ],
  },
  {
    section: 'Entreprise',
    links: [
      { name: 'Helios Industrial Components', url: '#' },
      { name: 'Contact', url: '#contact' },
      { name: 'Confidentialite', url: '#' },
    ],
  },
];

const socialLinks = {
  facebook: 'https://www.facebook.com/',
  x: 'https://twitter.com/',
  github: 'https://github.com/mearashadowfax/ScrewFast',
  google: 'https://www.google.com/',
  slack: 'https://slack.com/',
};

export default {
  navBarLinks,
  footerLinks,
  socialLinks,
};
