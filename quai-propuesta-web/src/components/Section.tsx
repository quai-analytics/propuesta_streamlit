import { ReactNode } from "react";
import { motion } from "framer-motion";

type SectionProps = {
  id: string;
  eyebrow?: string;
  title: string;
  description?: string;
  children?: ReactNode;
  dark?: boolean;
};

export function Section({
  id,
  eyebrow,
  title,
  description,
  children,
  dark
}: SectionProps) {
  return (
    <section
      id={id}
      className={`py-20 ${dark ? "bg-slate-950" : "bg-slate-900"} border-b border-slate-800`}
    >
      <div className="mx-auto max-w-6xl px-6">
        <motion.header
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.5 }}
          className="max-w-3xl"
        >
          {eyebrow && (
            <p className="text-sm font-semibold tracking-wide text-quai-teal uppercase mb-2">
              {eyebrow}
            </p>
          )}
          <h2 className="text-3xl md:text-4xl font-semibold text-slate-50 mb-4">
            {title}
          </h2>
          {description && (
            <p className="text-slate-300 leading-relaxed">{description}</p>
          )}
        </motion.header>
        {children && <div className="mt-10">{children}</div>}
      </div>
    </section>
  );
}


