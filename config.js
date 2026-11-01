/*
  Ligação com o banco da agenda (o mesmo Supabase da agenda da Amanda).
  Só a chave PÚBLICA pode ficar aqui ("Publishable key", começa com sb_publishable_).
  NUNCA coloque aqui a "Secret key" nem a "service_role".
*/
window.SUPABASE = {
  url: "https://qumfluviiqjxlqzjcfly.supabase.co",
  anonKey: "sb_publishable_VzXwyl7KzD3EXx0QtHT9ww_BRCm-KW-"
};
// WhatsApp do salão (a confirmar com a Sandra), com DDI e DDD, só números
window.SALAO = { whatsapp: "5511967682546" };
